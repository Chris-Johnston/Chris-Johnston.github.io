---
layout: post
title: Hacking the Moen Flo IoT leak sensors
description: I bought some IoT leak sensors and dumped the firmware.
date: 2021-07-01
---

# Hacking Moen Flo leak sensors

I bought some Moen Flo sensors and threw them around, since I have a sink which
used to leak. These are wifi-connected IOT sensors which beep and send a notification
to the Flo app if they detect water.

To set these up, the cover twists off to reveal the circuitboard with a pull tab and reset button.
This revealed that it runs on an ESP32 or similar MCU, and that the board has exposed serial pins
on an unpopulated header!

![](/images/flo/setup.png)

Once I saw this, I left a unit behind and didn't update the firmware. I wanted to see
if there was anything interesting I could do using the state out of the box.

## Connecting to serial

I used a normal FTDI usb-serial cable and some jumper wires to plug into the programming
interface. When the device was turned on, I saw messages on the console!

![](/images/flo/serialConnect.png)

![](/images/flo/imin.png)

Even better, there's a CLI! There's not much that can be done on it, other than dumping the configured SSID,
configuring some settings, and running some test modes.
The CLI does timeout after some amount of time.

```
/FloSystem(600553) flo_system_deep_sleep<flosdk/system.c:139>: flo_system_deep_sleep: go into deep sleep mode
```

![](/images/flo/2023-02-07-21-53-10.png)

note: _wonder if we can manipulate the root CA here_

![](/images/flo/2023-02-07-21-53-26.png)

I don't consider this to be a security flaw. If you're physically able to reach my IOT sensors, you could just as easily plug
into my network.

## We have to go deeper

So a device CLI is cool. What else can be done?

![](/images/flo/magic100pin.png)

If the magic "100" pin is jumped to ground, the device will enter a bootloader mode.
This causes the onboard LEDs to stay off, so it looks like nothing works.

But, I can use esptool to dump the firmware.

![](/images/flo/2023-02-07-21-50-42.png)

Thankfully, the normal device CLI dumps the partition table on boot.

<!-- todo get a better screenshot of this -->
![](/images/flo/2023-02-07-21-50-16.png)

## (Somewhat) OSINT

If I had more experience I would have done this in ghidra, but while having
trouble setting it up, I just ran `strings` on it, and found a bunch
of useful info anyways.

I found someone's username, in the form `{firstName}{lastName}`.

![](/images/flo/2023-02-07-21-54-42.png)

And I found their LinkedIn

Unfortunately I got to them too late (they quit September 2021), I hope they are enjoying their new job

![](/images/flo/2023-02-07-21-55-38.png)

and cool, here's a bunch of information about how this device was made:

and from their profile I could get more info about how the device was made, like how it is running FreeRTOS (didn't know this)

FreeRTOS would explain why there's a ton of code in here which seems
to be out of scope, since it's a whole OS and not just a dumb baremetal thing.

## Now What?

I lost steam on this project because I got busy, and hit some roadblocks.

- wanna set this up in ghidra
  - esp32 support is limited? https://olof-astrand.medium.com/reverse-engineering-of-esp32-flash-dumps-with-ghidra-or-ida-pro-8c7c58871e68
  - could emulate this with qemu?? weeeeeird https://github.com/Ebiroll/qemu_esp32
- what else is the device cli hiding
- what mysteries are there in the firmware upgrade process
- are there any mysteries in the way it's networked?

