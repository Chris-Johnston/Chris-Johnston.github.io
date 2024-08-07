---
layout: page
permalink: /6861636b746865706c616e6574/lol
description: Internal Server Error.
---

This is a temporary site until the [GitHub repo](https://github.com/Chris-Johnston/CrowOfJudgement) and actual page is made public.

# Build Guide

Hello! If you are reading this, it means that you are the lucky recipient of the item. Great!
If the event is still in progress do not disclose what is mentioned in this post.
I will make a more detailed post that isn't as vague once things are over.

**Do not open the item or proceed ahead until otherwise instructed.**

Instructions are listed below.

<div style="height: 3000px;"></div>

## Parts

It is time to open your package. You should see the following:

![Image of parts.](/images/etc/DSC04722small_.png)

You should have:
  - The really obvious part
  - 2 LEDs (red)
  - 2 surface-mount resistors (40 ohm 1206 package)
  - 1 surface-mount switch
  - 1 coin-cell battery holder for a CR2032
  - (If it arrives in time) a CR2032 battery

This page will provide some non-specific details for how to assemble the item.

## Tools Required

You'll need:
  - A soldering iron with a relatively fine tip
  - Solder
  - A room with good air circulation

Nice to have:
  - Diagonal cutters
  - Tweezers or pliers
  - Solder wick

# Assembly

## 1. Surface Mount Parts

The surface mount parts are the hardest part, luckily there aren't that many of them. It's good to get them out of the way first.
The challenge with these parts is that you have to keep them steady in the right place.

In general the technique I use is:
1. Tin one pad of the package very slightly.
2. Line up the package, ideally with tweezers or pliers.
3. With one hand heat the tinned pad and with the other hold the package in place.
4. Once the package is secure, solder the remaining pads. (In this case there are only 2.)

That's what I do here with the switch. I would actually recommend instead starting with the resistors, since I gave you 2, but the switch is
a bigger package so it will be easier.

Tin one pad for the component.

![Tin one side of the footprint for the switch.](/images/etc/DSC04725web.png)

Place the part in place, hold it steady with the tweezers, heat up the pre-tinned side, then solder the other side.
The switch is not directional, so it can go either way. Neither are the resistors.

![Solder the other side of the switch.](/images/etc/DSC04726web.png)

The switch should stand up a little bit. Unfortunately the part I picked kinda sucks. It sticks out from the board, and the switch is flush in the casing.
You will need a screwdriver or a pencil to flip the switch back and forth.

Next, I soldered the resistor. They are not directional, so don't worry if the numbers don't add up.
I gave you 2 because they are very tiny.

![Solder the resistor.](/images/etc/DSC04727web.png)

If it turns out that the pads have too much solder, that's why solder wick is handy.

Congrats! That's the hard part!

## 2. Through-Hole Parts

Next up are the through-hole parts. If you know how to solder, you know how to solder these. If you don't for some reason, there are many guides or you can just DM me.

Both of these parts are directional. If you mess up everything completely in reverse, it will probably still work, but if any less then it won't work.

Start with the battery holder.

![Place the battery holder.](/images/etc/DSC04731web.png)

The square side of the battery holder goes on the **+** end, facing outwards on the **back** of the board. Place the board down on the battery holder and solder the two pins.

The battery holder pins are very sharp, and are in an area where you might place your hand! Be sure to trim the pins off when you are done so they aren't so sharp!

_This goes without saying, but you are also probably soldering with lead. Please don't lick the board, because lead isn't good for you._

All that's left are the LEDs.

You will probably know this already, but it's good to double check. LEDs have a flat edge on one side, one leg which is shorter, and you can also check what the inside of the LED looks like. **Match up the short leg (-) with the square hole (also labelled - on the back)!**

![LED placement.](/images/etc/DSC04732web.png)

When soldering the LEDs, you may want to bend the pins a bit so that the LED stays in place. Even when pulled tight, it will have a small amount of wiggle room for adjustment. Be sure to trim these pins as well.

_Note:_ If the switch turns out to be really bad, you could probably use one leg of the LEDs to jump the two pins for the switch in its place. This will leave things permanently on.

## 3. Insert Battery

That's it! All that's left is to insert the battery. It should go in only one way, with the positive end of the battery facing outwards.

# Some Things You Should Know

- The holes in the top are meant to run thread through to hang it up as an ornament. I may or may not have provided something for this. We'll see. It will likely be off-balance because of the battery.

- The LEDs are super bright, I have not done the math for how long it will stay on. I doubt it will be very long. Turn it off when you are done, or prepare some extra CR2032 batteries.

- The 3v3 and GND pins in the corner are meant to be an external power source. Want to hook this up to an Arduino? Go ahead!