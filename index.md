---
layout: home
title: chris-johnston.me
---

This is a site that I use to highlight projects that I've been working / have
worked on, when more than a README is needed.

To see my [portfolio of the games I've worked on, click here.]({{ site.baseurl }}/games-portfolio)

This page is very inconsistently updated. To see what I'm currently working on
you'd be better off looking at
 [what I have posted on my GitHub page. Username: Chris-Johnston.][cjgithub]

Here are some of the projects I've worked on:

![Binary keyboard on hackaday](https://chris-johnston.me/images/binarybuild/hackaday.jpg)

  - The Binary Keyboard. It's a mechanical backlit keyboard that types
  in binary. It also has a screen. [Git Repo][binkeyboardgit] [Build Log]({% post_url 2017-04-21-binary-keyboard-build-log %})
  
<iframe width="300" height="315" src="https://www.youtube.com/embed/rzU7GU4T2Bk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
  
  - The Internet Xmas Tree. I used a Raspberry Pi and some Neopixels to control
  my Xmas tree. This was exposed to the Internet and people were invited to customize the lighting of our tree. [I later did (more or less) the same thing on the front porch.][patiogit]
  [Internet-Xmas-Tree Git Repo][xmasgit] [PatioLightsHost Git][patiogit]
  
  ![Discord Achievement Bot](https://camo.githubusercontent.com/fc6534de713b13e051180bfc2707a8440758be58/687474703a2f2f692e696d6775722e636f6d2f396c7a7778366a2e676966)
  
  - Discord bots. I have a few, which are suited for different purposes.
    - I have some written in C# and Python(3.6) intended for
    collaboration with my peers and other miscellaneous utilities for our servers.
    [CSSBot C# Git Repo][cssbotgit] [CSSBot Python Git Repo][cssbotpygit]
    - Using Magick.NET, I made [a bot to generate xbox-styled achievement popups.][achievementgit]
    - I also have [contributed to the Discord.NET library.][dnetcontrib] I've done refactoring, unit tests,
      developed new functionality, and helped contribute to the documentation.
  - I made a minimal [reverse-engineered library for driving Chinese knockoff IOT lightbulbs using Wireshark.][bulbgit] Currently it can turn lights on and off in any color.
  - I [(occasionally) develop a Python library called Easier68k for assembling, disassembling and simulating the Motorola 68K processor][easier68k] to replace legacy software that was used at by school, with the goal of more flexible
  functionality and much better cross-platform support.
 
![Laser cut hackathon trophies.]({{ site.baseurl }}/images/uwbhackstrophy.jpg)
  
  - I contributed to my school's hackathon, by providing example code for
    [Discord, Twitter, and Spotify bots in Python and C#][uwbhacks-barebones]. I also
    [wrote up documentation and included relevant topics in our documentation.][uwbhacks]
    During the event, I lead the group of tutors to help participants with coding questions.
    - I also laser cut these trophies.
    
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4v70QhtXlvY?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

 - I worked in a team to make a game in my Introduction to Game Development class. [It's called Grappel, and can be found here. Try the web build!][grappel] We were voted as one of the most popular games in our class.
 
  - While I am not a web design expert, [this site uses my own Jekyll style, called names_are_hard, which you can find here.][names-are-hard]


[cjgithub]: https://github.com/Chris-Johnston
[binkeyboardgit]: https://github.com/Chris-Johnston/BinaryKeyboard
[patiogit]: https://github.com/Chris-Johnston/PatioLightsHost
[xmasgit]: https://github.com/Chris-Johnston/Internet-Xmas-Tree
[cssbotpygit]: https://github.com/Chris-Johnston/CSSBot_Py
[cssbotgit]: https://github.com/Chris-Johnston/CSSBot
[dnetcontrib]: https://github.com/RogueException/Discord.Net/pulls?utf8=%E2%9C%93&q=author%3AChris-Johnston+
[achievementgit]: https://github.com/Chris-Johnston/DiscordAchievementBot
[bulbgit]: https://github.com/Chris-Johnston/PythonWifiBulb
[uwbhacks]: https://uwb-acm.github.io/Hackathon-Docs/
[uwbhacks-barebones]: https://github.com/UWB-ACM
[uwbhacks-trophy]: {{ site.baseurl }}/images/uwbhackstrophy.jpg
[easier68k]: https://github.com/Chris-Johnston/Easier68k
[grappel]: https://grappel.ninja
[names-are-hard]: https://github.com/Chris-Johnston/names_are_hard
