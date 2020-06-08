---
layout: post
title: Patio Lights
description: Internet-enabled animated RGB Halloween/Xmas/etc. lights.
github_url: https://github.com/Chris-Johnston/PatioLightsHost
github_short: Chris-Johnston/PatioLightsHost
date: 2018-10-30
image: /images/patio.gif
---

After working on the [Internet Xmas Tree]({% post_url 2018-12-25-internet-xmas-tree %}), 
we decided that the next logical step from this would be to create
multipurpose lighting for the front porch.

Most of October that year was spent working on these lights, which were just
finished before Halloween.

Unlike the tree, this project incorporated a lot more hardware,
which made developing this system a lot trickier.
On the night of Halloween, we ran strips of LEDs both on the inside and outside
of the railing.

![Picture of lights on both sides of the railing.](https://raw.githubusercontent.com/Chris-Johnston/PatioLightsHost/master/resources/halloween1.jpg)

In addition to driving all of these LEDs, we installed 3
knock-off brand RGB lightbulbs and would control those using the same system.
These bulbs were [using my reverse-engineered library](https://github.com/Chris-Johnston/PythonWifiBulb)
that I created to replace the Android app.

One bottleneck that I discovered with the tree was how much processing power
was required to drive all these LEDs (with very strict timing needs) and
animate their colors, all while hosting a webserver.
In addition, rebooting the Pi meant that the lights would be stuck until
it could restart the driver program.

Because of these reasons I decided to use an Arduino Mega to drive these
LEDs. The Pi now only sets the parameters for the lights, like the colors
and patterns, and the Mega handles drawing them all. This reduced the load
on the Pi, and I think made the entire system much more robust.

There were some issues with serial communication, since drawing the LEDs
turns off interrupts. Messages were often repeated a number of times to ensure
that they worked.

## A Few Months Later

![Image of the Seahawks pattern.](https://raw.githubusercontent.com/Chris-Johnston/PatioLightsHost/master/resources/seahawks2.jpg)

After leaving the system in place for a few months, everything seemed to work
fine. We didn't even cover the plastic container that housed the Pi or the
Arduino. I'm actually still amazed that they survived for so long.

While the Neopixel strips did claim that they were water resistant
and came in a special rubber cover, after a while we had some LEDs that
became faulty. While dead pixels aren't a big deal for most LED panels,
given that these are all chained together meant that entire segments of the LED
strip could be inactive.

## A Year Later

A year later we had found that the remainder of the LED strips had died, and that
we'd end up getting brand new ones to replace them.

Amazingly, the Arduino and Raspberry Pi that we had left outside for that long
still worked just fine (after letting them dry out). All of the plastic on the Pi
had yellowed, but otherwise it didn't seem to have any issues.