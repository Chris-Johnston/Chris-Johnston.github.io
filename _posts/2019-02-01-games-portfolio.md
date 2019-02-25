---
date: 2019-02-01
layout: post
title: Game Projects
description: A listing of the games I've made for classes and Game Jams.
tag: project
permalink: /games/
---

Here are some of the games that I've worked on.
[The broader scope of software projects (not just games) that I've worked on can be found on the Projects page.]({{ site.baseurl }}/projects)

# PGTRTKD3000DGOTY (Fall 2018)

![Logo of PGTRTKD3000DGOTY](https://chris-johnston.me/PGTRTKD3000DGOTY/index_files/logo_small.png)

![Screenshot of PGTRTKD3000DGOTY]({{ site.baseurl }}/images/games-portfolio/pgtr.png)

### [Play now at https://chris-johnston.me/PGTRTKD3000DGOTY/](https://chris-johnston.me/PGTRTKD3000DGOTY/)

[Source code hosted on GitHub.](http://github.com/Chris-Johnston/PGTRTKD3000DGOTY)

**Pet GTR Turbo Kart Drift 3000 _!!!_ Deluxe Game of the Year** (or **PGTRTKD3000DGOTY**, for short) is an online pet training game
similar in concept to a Tamagotchi.
The goal of the game is very simple, adopt a pet and keep training it to improve it's abilities. Then, race
it for the best time to get placed on the top of the global leaderboard.

This was a final project in both my Cloud Computing and Database classes.
Our requirements were to create an application:
- Hosted using public cloud services, like Azure or AWS.
- That is interactive.
- That stores data in a database, like MSSQL.

In a group of 3, we created this application using ASP.NET Core in C#, hosted on Azure App Services.
_(The current version is completely static, for the sake of demonstration.)_
We used Bootstrap CSS, Typescript, and Razor pages to build out front-end.

I was in charge of:
- Managing the project as a whole, among my two other group members.
- Setting up our CI/CD pipeline using Azure App Services, so that we could effortlessly release code.
- Administering to our production and testing MSSQL databases, hosted in Azure.
- Putting out fires related to our front-end, like setting up a Typescript build pipeline,
or registering our domain name.
- The "amazing" art assets that this game has to offer. (Including that logo, which I'm very proud of.)
- Extensive code review on every feature that was implemented, and managing tasks on GitHub.
- Developing a secure authentication flow using a HMAC SHA256 hashing algorithm.
- Integrating with third party services, like Twilio for SMS notifications, and Discord
for webhook notifications.
- Designing and implementing the race game, as well as the training mechanics as a whole.
- Writing unit tests, where we could easily do so.

# Grappel (Spring 2018)

### [Play now at https://grappel.ninja !][grappel]

[Source code hosted on GitHub.][grappel-gh]

[grappel-gh]: https://github.com/Chris-Johnston/Grappel
[grappel]: https://grappel.ninja/

Grappel is a physics-based platformer in which your 
objective is to skillfully manuever through several
challenging levels. As a bonus, there's an 
endurance mode which was designed to test your
mechanical skill of swinging, gaining, and maintaining
momentum as you fly across the screen.

![Screenshot of Grappel gameplay.][grappel-gameplay]

<iframe width="75%" margin="10px auto" height="300px" display="block" src="https://www.youtube.com/embed/4v70QhtXlvY?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

I worked on this project with a group of my student
peers in an agile team for our Introduction to Game Development class. We used the Unity game engine in C#.

I was responsible for:

- The initial ideas and design of the prototype, and 
trying out new ideas based on playtest feedback later on.
- Overseeing code reviews and Pull Requests on GitHub.
- Implementing and tuning the physics interactions.
- Xbox 360 controller support.
- Building and releasing our game (Linux, Windows, and Web) on our AWS-hosted Ngnix website. This included making the website and the trailer video.

[grappel-gameplay]: {{ site.baseurl }}/images/games-portfolio/grappel_gameplay.png

# Kelvin 373 (Winter 2018)

### [Play now at https://fantasticpineapplebrotherhood.fun][fpb]

[Source code hosted on GitHub.][fpb-gh]

Kelvin 373 is a boss-rush platformer in which the player's skills are tested against two bosses.

![Screenshot of Kelvin 373 gameplay.][fpb-sc]

This was a group project with my student peers for our Game Engine Development class, where our focus was on 
developing a game engine using a HTML5 canvas and Javascript.
We developed the fundamentals of the game engine, including:
- A spritesheet-based animation system, and a particle system.
- Handling and extending user keyboard input.
- Developing OpenGL shaders.
- Implementing the core 'game-loop' functionality.

For this project, I:
- Oversaw code reviews using GitHub.
    - Some group members were completely new to using Git, so I assisted in teaching them how to get started.
- Set up HTML and Javascript linters, using Travis CI.
- Contributed a second level where the player fights against a self-replicating boss.

[fpb]: https://fantasticpineapplebrotherhood.fun/
[fpb-gh]: https://github.com/Chris-Johnston/CSS452Game
[fpb-sc]: {{ site.baseurl }}/images/games-portfolio/fpb.png

# Hunt the Wumpus (2015)

As part of a Microsoft-hosted event for AP Computer Science highschoolers, I participated
in a team of 4 with other students to develop a "Hunt the Wumpus" game.
My team placed 1st runner up out of all the other schools in the area that participated,
and were the only team at my high school that won an award.

![Hunt the Wumpus main menu.]({{ site.baseurl }}/images/games-portfolio/wumpus_mainmenu.png)

![Hunt the Wumpus gameplay.]({{ site.baseurl }}/images/games-portfolio/wumpus_gameplay.PNG)

Users would navigate a randomly-generated maze to hunt down the Wumpus.

![Hunt the Wumpus trivia.]({{ site.baseurl  }}/images/games-portfolio/wumpus_trivia.PNG)

At it's core, the game was based on trivia. Many types of interactions prompted the user to answer
randomly-chosen questions. The color-coded answers would correspond to the face buttons of Xbox 360 controllers.

We made a first-person 3D game using the Unity engine. I created art assets using the modeling software
Blender.

![Hunt the Wumpus art.]({{ site.baseurl }}/images/games-portfolio/wumpus_art.png)

I took on many of the assigned roles for this project, including the art and graphics, maze generation,
core gameplay loop, and trivia.

I developed an algorithm for generating a cave system with a set of rooms, where none of the 
rooms were disconnected.

![Hunt the Wumpus maze generation.]({{ site.baseurl }}/images/games-portfolio/wumpus_cavegen.PNG)

Users could re-generate as many cave patterns as they wanted, and even choose their own random seed.
This would be their level for the game.

# Game Jams

I've participated in a number of Hackathons and Game Jams since 2015.

Here are some of the games I've made from these:

## Low Battery (August 2015)

[Part of the GB Jam 4 game jam. View the submission here!](https://gamejolt.com/games/low-battery/87008)

You play as a gameb--err handheld game console that is in desperate need of a fresh set of batteries. As you move, jump, or even do nothing at all, your battery levels will drain. If you run out of battery, you will lose.

I used this game jam as an opportunity to learn the MonoGame game engine for the first time. I expanded upon the platforming
genre by adding the battery mechanic which requires that the player keep moving, but be conscious of their failed attempts.

![Low battery gameplay screenshot.]({{ site.baseurl }}/images/games-portfolio/lowbattery.png)

## Operation Peeps (May 2015)

[Part of the Ludum Dare 32 - "An Unconventional Weapon" game jam. View the submission here!](http://ludumdare.com/compo/ludum-dare-32/?action=preview&uid=52345)

This was my first-ever game jam, where I set out to better familiarize myself with Unity.
I created all of the assets, from scratch, in less than 48 hours.

I built a wave-based first-person-shooter in which the "unconventional weapon" shot Easter Eggs at
mashmallow Peeps.

![Screenshot of Operation Peeps gameplay.]({{ site.baseurl }}/images/games-portfolio/operationpeeps.png)
