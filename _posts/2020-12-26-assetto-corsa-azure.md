---
layout: post
title: Hosting an Assetto Corsa multiplayer server on Azure
description: Here's how I set up an Assetto Corsa server running on an Azure VM.
date: 2020-12-26
---

# (draft)
High level steps:
1. make a linux vm in azure
2. setup steamcmd
3. download assetto corsa dedicated server

# Create an Azure VM

![Create the Azure VM.](/images/acds/create_azure_vm.png)

I'm using latest Ubuntu server LTS because that's my preference.

Going with the B1ms spec server with 2 gb of ram. Will report how well that does.

I recommend using a SSH key based authentication.

For now, leave the inbound port rules using the defaults, so let 22 (SSH) enabled. We'll enable more later.

![Configure the auto-shutdown settings.](/images/acds/mgmt_auto_shutdown.png)

Note that by default, auto-shutdown is enabled.
In my case, I know that I won't always be running this server 24/7, and so this is actually a decent way to save on hosting costs for when I forget to shutdown the VM.
If you want a more available server, I would recommend shutting this off.

# Setup SteamCmd

Log into the server using the public IP address.

The valve developer wiki provides some great instructions for installing SteamCMD, which I would also recommend.

https://developer.valvesoftware.com/wiki/SteamCMD

Some notes:
I had to run `sudo dpkg --add-architecture i386` before I could run `sudo apt install steamcmd`.

Note that we very well could be running this in docker if we wanted to, but in this case I didn't feel that there was a need. It also seemed that these images were community-maintained instead of from Valve themselves.

https://steamcommunity.com/app/244210/discussions/0/2828702373004724010/

I used this guide once steamcmd was installed.

After it's installed:
```
$ steamcmd
...
<bunch of logs go here>
...
Steam Console Client (c) Valve Corporation
-- type 'quit' to exit --
Loading Steam API...OK.

Steam>
```

Login:
```
Steam> login <username>
```
cwd is /home/steam
```
Steam> force_install_dir ./assetto/
```

Install ACDS:
```
Steam> app_update 302550 validate
```

This did not work "ERROR! Failed to install app '302550' (Invalid platform)"

 instead ran: steamcmd +@sSteamCmdForcePlatformType windows

 ```
Steam> login <username>
Steam> app_update 203550 validate

 ```

 Despite "force platform type", works just great on linux!

 # Setup AC

 Try running the server once
 cd ~/.steam/steamcmd/assetto/
 ./acServer

 Should probably break, but that means it worked!

 Configure your server using
 nano cfg/entry_list.ini # the AI cars

 notable settings:
 ```
UDP_PORT=9600
TCP_PORT=9600
HTTP_PORT=8081
 ```

# Allow our game ports 

Allow the ports that we need

![allow ports in azure](/images/acds/add_port_settings.png)

# Send it!

Run the server and it should be able to phone home.

![working server](/images/acds/working_server.png)

![server list](/images/acds/server_in_serverlist.png)

![connected to server](/images/acds/connected_to_server.png)

# Automatically starting the server on server boot

It's great that we can manually start the server when we need it, but
in case our VM restarts, how do we start the process automatically?

# Configuring the game server

While you can edit the ini files directly, it's much easier to just use the GUI to do it.

I found that I had to install the DS, copy the game files to be under the Steam Assetto Corsa install directory,
and then I could copy the config onto my main machine, specify settings,
and then update the server.

