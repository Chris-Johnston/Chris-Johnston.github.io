---
layout: post
title: Hosting an Assetto Corsa multiplayer server on Azure
description: Here's how I set up an Assetto Corsa server running on an Azure VM.
date: 2020-12-26
---

**DRAFT: This page is incomplete and has a few more things to fix.**

[_Assetto Corsa_](https://store.steampowered.com/app/244210/Assetto_Corsa/) is a racing simulation game which supports online multiplayer play.
All of the lobbies are community-run. I wanted to set up a
private server to play among some friends, and so here's how I did it.

You can definitely host this server on the same machine you play on!
I chose not to do that so that everyone gets a fast connection to the server,
independent of my internet speed, and so that I can keep the server on
when I shut my machine off.

There are also places that will happily host servers for you, at a price.
But, I have some free credits for server hosting, and so the low low cost of free
is preferred.

**TL;DR:**
1. Create an Ubuntu VM in Azure
2. Setup SteamCMD, download Assetto Corsa Dedicated Server
3. Allow specific ports through firewall
4. Configure server and go

# 1. Create an Ubuntu VM in Azure

Of course, any cloud VM would do just fine here. Here are the steps
I followed to set this up in Azure.

![Create the Azure VM.](/images/acds/create_azure_vm.png)

While Assetto Corsa on PC is Windows-only, the server works on Linux too.
I created a new Azure VM running the latest Ubuntu LTS release, since it's what
I like to use.

I used the `B1ms` spec server with 2GB of memory. After testing this for a few hours
with a group of 4, this SKU handled great. **TODO: Investigate if I can scale down to save some spending.** (This could be overkill, I'm seeing it peaked around 14% CPU? Forums suggest network is the bottleneck, I wonder how much memory matters as well.)

I recommend using SSH-based authentication, instead of password-based.

The default inbound port rules are fine to start. I left port 22 (SSH) enabled so that I can log in. The necessary ports for the server can be enabled once we get them from the config.

![Configure the auto-shutdown settings.](/images/acds/mgmt_auto_shutdown.png)

Note that by default, auto-shutdown is enabled.
In my case, I know that I won't always be running this server 24/7, and so this is actually a decent way to save on hosting costs for when I forget to shutdown the VM.
If you want a more available server, I would recommend disabling this setting.

# 2. Setup SteamCmd, download Assetto Corsa Dedicated Server

SSH into the server using the public IP address.

[The Valve Developer Wiki provides some some great instructions for installing SteamCMD, as well as documentation in general.](https://developer.valvesoftware.com/wiki/SteamCMD)

Note that this first line was necessary, since I was running a 64-bit VM.
```bash
$ sudo dpkg --add-architecture i386
$ sudo apt update
$ sudo apt install steamcmd
```

The wiki also mentions that this can run in Docker. In this case I didn't feel it
was necessary. These images are also community-maintained instead of from Valve
themselves. It's just more straightforward to run it on the VM normally.

[This guide on the steam community for Assetto Corsa was helpful.](https://steamcommunity.com/app/244210/discussions/0/2828702373004724010/)
Once SteamCmd was installed, I ran the following commands.

```
$ steamcmd +@sSteamCmdForcePlatformType windows
...
<bunch of logs go here>
...
Steam Console Client (c) Valve Corporation
-- type 'quit' to exit --
Loading Steam API...OK.

Steam> login <username>
...
<password prompt goes here>
...
Steam> force_install_dir ./assetto/
Steam> app_update 302550 validate
```

`302550` is the AppId of the Assetto Corsa Dedicated Server.

I ran into this issue when I failed to include the `+@sSteamCmdForcePlatformType windows` arg. This happened even though this was on a Linux VM.

> ERROR! Failed to install app '302550' (Invalid platform)

To fix this, I made sure to include this parameter when starting the SteamCMD CLI.

Once this was finished, the game files were available under the directory `~/.steam/steamcmd/assetto/`

The `acServer` executable in this directory is the game server.

# 3. Allow specific ports through firewall

Assetto Corsa Dedicated Server by default uses the ports 9600 and 8081 with
both TCP and UDP. These are specified in the `cfg/entry_list.ini` server config file.

![allow ports in azure](/images/acds/add_port_settings.png)

This was added from the `Settings > Networking` tab in Azure.

# 4. Configure server and go

Once ports have been allowed, the ACDS should be able to "phone home".
The following output is what the logs should look like on success:

![working server](/images/acds/working_server.png)

The "phone home" step allows for the central Assetto Corsa server to know about your server
and so players can now search for your server using the in-game server browser window.

![server list](/images/acds/server_in_serverlist.png)

And if everything's configured correctly, players should now be able to connect without any trouble.

![connected to server](/images/acds/connected_to_server.png)

## TODO:

incomplete

# Automatically starting the server on server boot

It's great that we can manually start the server when we need it, but
in case our VM restarts, how do we start the process automatically?

# Configuring the game server

While you can edit the ini files directly, it's much easier to just use the GUI to do it.

I found that I had to install the DS, copy the game files to be under the Steam Assetto Corsa install directory,
and then I could copy the config onto my main machine, specify settings,
and then update the server with SCP.