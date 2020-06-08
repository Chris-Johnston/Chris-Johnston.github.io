---
layout: post
title: Adventures in Home Automation and DIY Security
date: 2020-05-27
categories: home-assistant
description: How I added (possibly too much) automation to my apartment.
image: /images/ha/rpi-servers.jpg
---

This is a summary of my experience setting up my own home automation
and security system using Home Assistant and ZoneMinder.

From anecdotal evidence about the problems with IOT,
I've successfully avoided this trend (for now):
 - My apartment uses a normal lock and key, not RFID.
 - As far as I know, all of my digital assistants are off.
   - I do have an Amazon Echo around somewhere, though I haven't taken it out of the box.
 - I'm not locked-in to paying a monthly fee to review footage captured by my security cameras.
 - Most of my lightbulbs are just regular single color lightbulbs.

I first started to mess with this stuff when I experimented with
[RGB IOT Lightbulbs, which I've written a bit about before here.][iot-lightbulbs] Maybe this was a slippery slope.

# The Initial Need for Security

I had just moved in to a new apartment, and wanted to set up some
sort of a security system for peace of mind while I'm out at the office.

I _absolutely_ did not want:
 - A monthly subscription for basic DVR functionality
 - A system that was insecure or publicly accessible

At a minimum, all I needed was a camera to record any activity that 
happens while I'm not home. Features like real-time notifications or
offsite backups were a plus.

# The Tools

Several free and open source solutions exist for addressing these needs.

## Home Assistant

[Home Assistant is an open source home automation platform][ha] that lets
you bridge together various services and devices using self-hosted infrastructure.
Many users run this on a Raspberry Pi.

I had first learned about Home Assistant from a talk at [LinuxFest Northwest.][lfnw]

I think the community support around Home Assistant is the best part.
[It integrates with tons of IOT devices and services.][ha-integration],

## ZoneMinder

[ZoneMinder is an open source video surveillance system][zm]
which can record from multiple IP cameras and detect activity.
It's meant to scale up for several cameras, but I only use it
to record video from a single IP camera.

While my IP camera does include a built-in record function which saves to an SD card, I don't want to depend only on that one card.
ZoneMinder enables me to backup footage on a more reliable server, but also monitor the status of any cameras I have connected.

### IP Camera Security

I definitely do not want my cameras showing up on Shodan.
To help remedy this, I've created a dedicated SSID just for IOT
devices, which isn't allowed to connect outside of my LAN.
Hopefully this will help prevent these devices from showing up
with a public IP, or from being able to "phone home."

## The Infrastructure

Both ZoneMinder and Home Assistant _can_ run on Raspberry Pis.
It's one of the recommended options for Home Assistant.

At one point, I had a stack of 3 Raspberry Pi's sitting on my desk,
running various services:

![Picture of 3 Raspberry Pis on my desk][{{ site.baseurl }}/images/ha/rpi-servers.jpg]

This worked okay for a while. It was clear that ZoneMinder could benefit
from something with a bit more power, luckily I was only using a single camera.
However, after less than a year with this setup, the SD card for that Pi completely
died. I'm not sure exactly what the cause might have been, but I speculate that the
amount of disk usage from ZoneMinder could have led to this.

I've since moved my ZoneMinder setup to a Debian server on an old Lenovo
desktop PC, with an actual hard drive. Moving off of an SD card has other benefits too,
I now have more storage capacity.

**Why not use a VM in the cloud?** This option could work, but for a few reasons I chose
against it. 
Currently I use 433 MHz radio connected to my Home Assistant Pi, which requires access to the GPIO.
ZoneMinder would generate a lot of traffic and more storage capacity is better, which an add to the expense
of a VM.
I already owned all of the equipment that I'm using, so the only operating cost is my electricity bill.

# Home Assistant + ZoneMinder = Profit?

At first it might seem that all I need is ZoneMinder to
monitor my IP camera while I'm out of the house.
I definitely could, but this poses a few issues:
 - How do I check this while I'm not home? Do I expose my ZoneMinder server on a public IP?
 - ZoneMinder does support some level of automation using cron jobs, but what happens if I deviate from a rigid schedule?

Home Assistant helps to address these issues.

Home Assistant's frontend is more robust than ZoneMinder's, so I feel better about exposing
this server publicly. In addition there are integrations available for 2FA, which is more than
ZoneMinder offers.
My router supports DDNS, so I'm also able to register a subdomain on my DDNS provider
and set up HTTPS certs.
With all of this, I can use Home Assistant's mobile-friendly interface or Android app
to access my camera remotely.
HA allows me to remotely toggle ZM's recording status, and can
let me view a timeline of detected events.

<!-- todo include a screenshot of the automation page -->

Using Home Assistant's mobile app, I can track my current location using my phone.
(Previously I used OwnTracks.)
With this, I set up an automation that starts recording on my cameras if I've been outside of a radius
surrounding my home for more than a few minutes.
And similarly, I set up the reverse to disable recording once I return home.

Once that was established, I could expand these automations
even further. When integrated with Twilio, I could use the
event detection in ZoneMinder to text myself images from the camera.
A great demonstration for why it's great to have this nearly all open-source ecosystem:
[I was able to implement parts of this feature in HA's Twilio plugin itself.][twilio-sms-media]

<!-- todo include a screenshot showing the blurred notification -->

# What else can Home Assistant do?

After using Home Assistant and ZoneMinder for a few weeks, I found it very useful for
checking on the status of my house while I'm away.
However, I had a few observations about the usability of this system so far:
 - The event detection in ZoneMinder was configured to be too sensitive, and would have false positives when the natural light through my blinds would change.
 - The ability to recall prior events still requires signing in to ZoneMinder, or relying on the Twilio notifications containing a useful frame of the recording.

In addition, one flaw of this system is that it doesn't allow me to verify that the door is locked.
On one occasion I had left the house in a hurry to realize upon coming home that I had forgotten to lock up.
While I don't anticipate this issue reoccuring, this peace of mind is nice to have.

## DIY IOT Door Monitor

[door-monitor] is the project I created to accomplish this.
(Note that I wasn't aware of ESPHome at the time, which seems like it could do everything here but better.)

It uses an ESP32 dev board connected to two reed switches which are taped on to the door frame and the door lock. When either one opens, the ESP32
wakes up from deep sleep mode and logs to a Flask server to collect this data.

![Image of the stuff taped to my door.]({{ site.baseurl }}/images/ha/installed_sensor.jpg)

![Image of the assembled board.]({{ site.baseurl }}/images/ha/assembled_board.jpg)

The Flask server acts as a proxy to forward this information along to
multiple sources, including Home Assistant but also a Discord webhook.
The Discord webhook was used as a faster and free alternative to Twilio SMS notifications.

![Image of the home assistant integration.]({{ site.baseurl }}/images/ha/home_assistant_integration.png)

Once this was integrated with Home Assistant, I could start doing some
pretty cool stuff with it.
Some automations that I had configured around this will text me if the door
or lock state changes if I'm away from the house, and also text me if I
have been away from the house for more than a few minutes without locking up.

![Image of notification sent if I forget to lock up.]({{ site.baseurl }}/images/ha/sms_notifications.jpg)

One clear benefit of this over ZoneMinder is that the notifications have
a much lower false positive rate. This way I'm inclined to trust the
notifications more and take action when I see them.

This system works great, just with a few downsides.
It looks vaguely like a bomb is taped on to my door which doesn't bother me
too much, but has raised an eyebrow when I had maintenance come by.
Also, while the ESP32 is known for being very power efficient, the dev
board that I use isn't. The system will happily burn through 4 AA batteries within a few weeks.
I plan on fixing the power consumption issue by using a TinyPICO board instead of a ESP32 dev module, apparently it's
3.3V regulator uses a lot less power.
Switching to rechargeable batteries has been a must.

[door-monitor]: https://github.com/Chris-Johnston/door-monitor

## Adding Sounds

[This video has been really inspirational for a number of projects I've done.][seinfeld-door]
At one point, I had set up a reed switch on a door in my school's lab, so
that one in every 30 times it was opened, it played a seinfeld bass riff
over the PA system in the room. We left it running for a few months.

Naturally I wanted the same thing at home. I was able to quickly spin up a
hacked-together Flask server (using the debug server, because it really doesn't matter)
to play sounds over a speaker when triggered over HTTP.
This fit together with the existing system really well.

This was extended to also serve as a way to play text-to-speech remotely.
Once I hooked it all up with Home Assistant, I could queue sounds
and say arbitrary text to a speaker sitting in my room.
Now, if the door opens while I'm away from home, the speaker can warn: `"Intruder alert! You are being recorded."`

[seinfeld-door]: https://www.youtube.com/watch?v=j8D8YjgnGR4

## Adventures with 433 MHZ RF

IOT lights are pretty cool, but their price isn't.
I'm not willing to spend a good chunk of change to buy smart bulbs
for everything in my house, since that price tag would add up quick.
Also, that just sounds like a headache.

But, being able to remotely switch lights on and off can be useful.
I ran across some 433 MHz switched outlets which are a much cheaper
approach for blinking lights on and off.

433 MHz radio is a pretty widely established standard for
universal garage door openers, cheap security devices like window reed switches, and more.
The Home Assistant community is aware of this, and has made efforts to
integrate with these cheaper devices.

There exist a few ways that they can connect HA to 433 MHz:
 - [RFLink]
 - Sonoff RF Bridge (usually flashed with Tasmota, a custom firmware)
 - Connecting a 433 MHz sender and reciever to the Raspberry Pi GPIO

Out of these, I chose to connect to the RPi GPIO.
This seemed to be the cheapest option, and potentially the easiest.

I'm not a fan of [RFLink], for a number of reasons. Their closed-source
approach seems to be causing them issues:

> Since some were asking, yes the project is still alive.
> However, we get way more support requests than we can handle

I like being able to contribute back to the tools that I use without
blindly emailing a random gmail address and waiting for a response.

[RFLink]: http://www.rflink.nl/blog2/

I decided against the Sonoff RF Bridge because I didn't want to deal with
flashing the Tasmota software. Also, I think at the time the devices were
out of stock.

I already was using a RPi, so just making a board to sit on the GPIO seemed like
the best solution.

### 433 MHz on Raspberry Pi

Home Assistant includes built-in integration with [rpi_rf], which
is a library for using RF with the RPi GPIO.
I found it really simple to configure.

However, in it's current state, the only issue I found was that
the Home Assistant integration doesn't (yet)
support receiving codes.
[It looks like there's some way to fix this, which I haven't tried fully yet.](https://community.home-assistant.io/t/rpi-rf-receiver-addon/32947)

To work around this, I've resorted to installing [pilight] and connecting
it to Home Assistant. This solution really doesn't feel ideal, since
I now have multiple ways to send RF codes, and I have to integrate with a
whole other service just to get RF working.

On the plus side, Home Assistant and [pilight] integrate with each other
pretty well.

[rpi_rf]: https://www.home-assistant.io/integrations/rpi_rf/
[pilight]: https://www.pilight.org/

# Houseplant Life Support

I have a couple of house plants.
Unfortunately, I forget to water them.
(There's a common trend behind these motivations.)

![Moe.]({{ site.baseurl }}/images/ha/moe.jpg)

In addition, because my place is somewhat dark, they need some extra light
from a fancy plant bulb. Using the 433 MHz wall switches from earlier,
I'm able to turn off this bulb with a timer, controlled by Home Assistant.
(The bulb produces an annoying high-pitched ringing noise, so I don't leave it on constantly.)

It would too easy just to make a reminder for myself to check the plants every
other day. This is why I created a sensor to monitor the conditions
of the plants. While I was at it, I also wanted to monitor the conditions
of the environment they are in, including temperature, but also CO2, since
I'll be staying indoors for a big chunk of 2020.

## ESPHome sensor board

ESPHome is a system for ESP8266/ESP32 that lets you integrate with sensors
and services by just writing some YAML. It's designed to integrate directly
into Home Assistant.

Some benefits that this has over something like my door monitor project:
 - Don't need to set up a proxy server to talk to HA, it handles that directly
 - Over the air updates
 - Dead simple to configure

In an afternoon I was able to solder up a board with a bunch of sensors:

![ESPHome sensor board for the plants.]({{ site.baseurl }}/images/ha/plant-sensor1.jpg)

I use soil moisture sensors that stick directly into the plant's soil to read out a relative
humidity. It outputs an analog signal corresponding to the humidity.
The value doesn't mean a whole lot unless it's calibrated, which I haven't bothered to do
carefully yet.

![Sensor sticking directly into the plant pot.]({{ site.baseurl }}/images/ha/plant-sensor2.jpg)

# What's next?

My TODO list for home automation stuff includes:
 - Setting up a 433 MHz RF bridge using ESPHome which should hopefully be more reliable
 - Setting up an IR LED bridge using ESPHome, so that I can control IR things in my apartment (even more) remotely
 - Reverse engineering the IR protocol used by my LG air conditioner, so that I can manage my AC (even more) remotely
 - Making at least one more plant sensor board, for other parts of the house

[iot-lightbulbs]: {% post_url 2016-10-12-hacking-a-lightbulb %}
[lfnw]: https://linuxfestnorthwest.org
[ha-integrations]: https://www.home-assistant.io/integrations/
[ha]: https://www.home-assistant.io
[zm]: https://zoneminder.com/
[twilio-sms-media]: https://github.com/home-assistant/core/pull/24971