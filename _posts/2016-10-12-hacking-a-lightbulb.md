---
layout: post
title: Hacking an IOT Lightbulb
description: How I reverse engineered the protocol used by some cheap WiFi lightbulbs, and made by own client application.
github_url: https://github.com/Chris-Johnston/PythonWifiBulb
github_short: Chris-Johnston/PythonWifiBulb
tag: project
---

I was given an internet-connected RGB lightbulb around the time that
I was working on the [Internet Xmas Tree]({% post_url 2018-12-25-internet-xmas-tree %}).
These bulbs were much cheaper than some of their counterparts, but
came with some significant downsides.

Unlike something like the Philips Hue, these can only be controlled
with their "Magic Home" app. It does the job, but is pretty clunky.

Using Wireshark, I was able to capture packets sent from the Android
app to the bulb. I used my laptop as a man-in-the-middle.

From these packets I was able to determine the data that was
being transmitted. I used Python to create a simple client that would
re-transmit the same data to the bulb. Initially this had some
significant issues and couldn't do anything more than change the
color, but I was able to continue adding features to it.

![Gif of FluxLed in use](https://camo.githubusercontent.com/1daddea3996f473f14cb9718b3e60d027f7ebf2c/68747470733a2f2f7468756d62732e6766796361742e636f6d2f4472656172794964696f746963466c79696e67666f782d73697a655f726573747269637465642e676966)

Using this custom client, I was able to build an application
to change the color temperature from this light, that could change
depending on the time of day.
[This project can be found at Chris-Johnston/FluxLight](https://github.com/Chris-Johnston/FluxLight)

I also used this client with the
[Patio Lights]({% post_url 2017-10-30-patio-lights %})
project, to control 3 lightbulbs. (Only 2 are visible in this GIF.)

![patio lights in use](/images/patio.gif)

## Other Clients

A while after I created my own client for controlling these lights,
I came across [Danielhiversen/flux_led](https://github.com/Danielhiversen/flux_led).
This project is a more complete implementation of the same work I've done.
Interesting that we chose a similar name, too.

I thought it was great that I could find this project that was
developed independently, as I had to make many assumptions that I couldn't
verify when I was reverse engineering the protocol.
I was glad to see that this project contained some of the same
magic numbers that I had found myself.