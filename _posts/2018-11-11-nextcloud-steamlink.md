---
layout: post
title: Hosting NextCloud on a Steam Link
date: 2018-11-11
categories: steamlink nextcloud
---

https://www.exploitee.rs/index.php/Steam_Link

After Dropbox discontinued support of encrypted ext4 file systems, I needed
an alternative file storage backup solution.

I've wanted to use NextCloud (previously OwnCloud) for a while now, but didn't
have a local dedicated server to use, and a raspberry pi wasn't as reliable enough.

Luckily, I did buy a Steam Link on sale for $2.50 (+ $7 shipping) during the latest Steam
sale, so I figure it's worth a try.

# 1. Rooting the Steam Link

This step is actually very easy, I followed this guide:
https://mcd1992.blogspot.com/2015/10/alright-this-was-lot-easier-than-i.html

1. Create the `enable_ssh.txt` file on a flash drive.
2. Power on the steam link with the drive plugged in.
    (I actually haven't used it before now, it was gathering dust on my shelf!)
3. `ssh root@<your ip>` with the password steamlink123

# 2. Setting up the Steam Link

We want to have ssh access without always having a usb stick plugged in,
and should have a non-root user.

Add a new user, and set a password

`adduser chris`

TODO: Getting issue where the filesystem is ro, so home cannot be mounted
TODO: missing usermod

Change the root password!!

`passwd root`

The startup script under `/etc/init.d/startup/S30sshd`
_will_ reset the root password, so either modify that file, 
or just don't restart the link with that usb in place.

Permanently enable root.

This script would start
`/usr/sbin/sshd`, so this should be added to the startup script at the very end

`vi /home/root/rc.local`

Then, reboot the device to verify that our changes worked.
`reboot -f`

Now, you should still be able to login to SSH without a USB drive connected.

