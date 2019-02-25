---
layout: post
title: Discord Bots
description: A brief summary of the work I've done with Discord Bots and the Discord API.
date: 2016-01-08
tag: project
image: https://camo.githubusercontent.com/fc6534de713b13e051180bfc2707a8440758be58/687474703a2f2f692e696d6775722e636f6d2f396c7a7778366a2e676966
---

I started making bots on Discord only a few months after joining the platform 
in 2016. Most are single-purpose applications that I just create for fun.
I either use the [Discord.Net][dnet] or [discord.py][dpy] libraries.

## Achievement Bot

[DiscordAchievementBot GitHub Repo](https://github.com/Chris-Johnston/DiscordAchievementBot)

This bot generates Xbox-styled achievement popups using Magick.NET.
At the time of writing, it's in nearly 200 servers with a total of 97,000 users.

## Discord.Net Contributions

I have contributed to the open source [Discord.Net][dnet]
library.

These contributions include:
- [Refactoring existing features](https://github.com/discord-net/Discord.Net/pull/743)
- [Updating the AppVeyor CI pipeline to support Ubuntu builds](https://github.com/discord-net/Discord.Net/pull/1157)
- [Significant design updates](https://github.com/discord-net/Discord.Net/pull/1004)
- [Adding unit tests](https://github.com/discord-net/Discord.Net/pull/967)
- [Improving command parsing](https://github.com/discord-net/Discord.Net/pull/943)
- [Updating the API to match new features](https://github.com/discord-net/Discord.Net/pull/1165)
- At one point hosting a backup of the documentation using AWS S3, when the primary site was unavailable

In addition to code review and
[other Pull Requests](https://github.com/discord-net/Discord.Net/pulls?page=1&q=is%3Apr+author%3AChris-Johnston&utf8=%E2%9C%93).

## CSSBot and CSSBot_Py

[CSSBot GitHub Repo](https://github.com/Chris-Johnston/CSSBot)
[CSSBot_Py GitHub Repo](https://github.com/Chris-Johnston/CSSBot_Py)

![Screenshot of CSSBot in use](/images/cssbot.png)

![Screenshot of CSSBot Py in use](/images/cssbot_py.png)

Originally created for a Discord server for my friends and other CSS students
at my school, these bots provide some all-around utilities.

I had made CSSBot first, but since C# wasn't widely known in the group,
I made CSSBot_Py using Python so that others could contribute.

[dnet]: http://github.com/discord-net/Discord.Net/
[dpy]: https://github.com/Rapptz/discord.py