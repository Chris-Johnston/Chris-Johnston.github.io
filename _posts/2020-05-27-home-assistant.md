---
layout: post
title: Adventures in Home Automation and Securty
date: 2020-05-27
categories: home-assistant
description: How I added (a bit too much) automation and IOT to my apartment.
---

The 'S' in "IOT" stands for "Security".

From knowing so much anecdotally about the problems with IOT,
I've successfully avoided this trend (for now).
 - My apartment uses a normal lock and key, not RFID with a master key.
 - As far as I know, no digital assistants around me are listening for keywords.
   - I have an Amazon Echo around somewhere, though I haven't taken it out of the box.
 - I'm not locked-in to paying a monthly fee to review footage captured by my security cameras.
 - Most of my lightbulbs are just regular lightbulbs.

I first started to mess with this stuff when I experimented with
[RGB IOT Lightbulbs, which I've written a bit about before on this site.][iot-lightbulbs] Maybe this was a slippery slope.

# The Initial Need for Security

I had just moved into a new apartment, and wanted to set up some level
of a security system for peace of mind while I'm out at the office.

I _absolutely_ did not want:
 - A monthly subscription for basic DVR functionality
 - A system that was insecure or publicly accessible

At a minimum, all I needed was a camera to record any activity that 
happens while I'm not home. Preferably, I'd like for near real-time
notifications, and the ability to back up this footage remotely
(should the physical server be stolen). Also, I find it a little creepy
to be always recording the inside of my house while I'm at home,
so it would be nice to turn off the camera if I'm at home.

## Home Assistant

[Home Assistant is an open source home automation platform][ha] that lets
you bridge together various services and devices using self-hosted infrastructure.

I had first learned about Home Assistant from a talk at [LinuxFest Northwest.][lfnw]

_So, what's so cool about it?_ I think the part that's my favorite is the
community support around it. [It integrates with tons of things][ha-integration],
including tons of IOT devices and services.

## ZoneMinder

[ZoneMinder is an open source video surveillance system][zm]
which can record from multiple IP cameras and detect activity.
It's meant to scale up for several cameras, but I only use it
to record video from a single IP camera.

While my IP camera does include a built-in record function which saves to an SD card, I shouldn't really depend on it.
ZoneMinder enables me to backup footage on a more reliable server, but also monitor the status of any cameras I have connected.

### IP Camera Security

I definitely do not want my cameras showing up on Shodan.
To help remedy this, I've created a dedicated SSID just for IOT
devices, which isn't allowed to connect outside of my LAN.
Hopefully this will help prevent these devices from showing up
with a public IP, or from being able to "phone home."

## Home Assistant + ZoneMinder = Profit?

At first it might seem that all I need is ZoneMinder to
monitor my IP camera while I'm out at work.
I definitely could, but this poses a few issues:
How do I check this while I'm not home? Do I expose my ZoneMinder server on a public IP?

ZoneMinder does support some level of automation using CRON jobs, but what happens if I deviate from a rigid schedule?

Home Assistant helps bridge this gap.

I can use the Home Assistant mobile-friendly interface to look through my cameras remotely.

In addition, HA can also change the recording status of
ZoneMinder to toggle between "Monitor" and "Record".

<!-- todo include a screenshot of the automation page -->

Using Home Assistant's mobile app, I can track my current location using my phone. With this, I set up an automation that starts recording my cameras if I've been outside of a radius
surrounding my home for more than a few minutes.
And similiarly, I set up the reverse to disable recording once I return home.

Once that was established, I could expand these automations
even further. When integrated with Twilio, I could use the
event detection in ZoneMinder to text myself images from the camera. A great demonstration for why it's great to have this nearly all open-source ecosystem: [I was able to implement parts of this feature in HA's Twilio plugin itself.][twilio-sms-media]

<!-- todo include a screenshot showing the blurred notification -->

# What else can Home Assistant do?

<!-- mention the door monitor, how it integrates with existing security tooling -->

<!-- door monitor solves false positives from the camera (natural light), and also solves leaving the door unlocked when I leave the house -->

<!-- also adds the sounds, which are fun -->
<!-- to do this, had to create a proxy server to forward sensor data on to HA and discord webhooks >

<!-- talk about connecting with IOT lights -->
<!-- IOT lights are expensive, 433mhz is cheap -->
<!-- tried to find a prebuilt bridge, but that's expensive and required work. might as well just make a hat for a pi -->
<!-- just built it using rpi rf, and pilight to recv (pilight really needs to be replaced) -->

# Home Assistant + DIY IOT

<!-- need to water my plants, so just use an esp to do it -->
<!-- previously for the door monitor, I had to spin up a proxy server which involved a lot of work -->
<!-- learned about esphome, basically lets you program esp32 with yaml in a way just like HA config -->
<!-- was super easy and now I have a bunch of sensors monitored with ota updates -->
<!-- next plan is to make a RF and IR bridge -->

<!-- todo: break down the type of hardware that I host home infra on -->
<!-- mention that zoneminder on a Pi died when the sd card died -->

[iot-lightbulbs]: todo
[lfnw]: https://linuxfestnorthwest.org
[ha-integrations]: https://www.home-assistant.io/integrations/
[ha]: https://www.home-assistant.io
[zm]: https://zoneminder.com/
[twilio-sms-media]: https://github.com/home-assistant/core/pull/24971