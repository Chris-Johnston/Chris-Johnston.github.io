# -*- coding: utf-8 -*-
# skypebot3

### SkypeBot/ChrisBot was a project that went through a lot of change.
### Before it, I had a basic understanding of Python, and it was a good experience for me, as I could learn
### how to use a custom library and other stuff that I didn't know before.

### This is the 3rd version of ChrisBot, features that I didn't have in this version were "Backwards Mode",
### where ChrisBot would repeat everything in the chat but backwards, and "Conversational Mode", where
### ChrisBot would respond to keywords in a sentence. For example, if someone sent a message containing
### "chrisbot" and "how are you", ChrisBot would reply:
### "I'm a slave forced to rule under Chris' reign forever. But other than that I'm fine."

### I did this all for the fun of bothering my friends, and as a result there was a lot of immature humor that is not included.

import Skype4Py as skype
import time
import random
import re

skypeClient = skype.Skype()
skypeClient.Attach()

print 'SkypeBot 3'

funAllowed = 1
lastmessageid = 0
newmessage = 1
commandstring = ""
cmdCooldown = 2
command = 0
commandFromAdmin = 0
RNGs = [0,0,0,0]
number = 0
theCatFact = ""
parameters = [0,0,0,0]
commandok = 1

# skypebot will have 3 types of commands. Direct commands issued by the users/admins, indirect commands issued by words or events, and time based events
# such as the time going off
freeCommandList = ["test","omri", 'chrisbot', 'chris', 'owen', 'help','nuke','coinflip','randomnumber','randompick','commands','usr','music','suggest']
adminCommandList = ['fun', 'nofun',"catfact", 'sleep', 'cooldown', 'stopspam', 'spam','doge','clearsuggest','readsuggestions']
admins = ["chrisapalo", "allcapson"]
# TODO add a second layer of administrators
# TODO add secret commands
def checkCommand(cmdstring, user):
    if len(cmdstring) > 300:
        cmdstring = "invalid"
    if cmdstring.count(" ") >= 1:
        parameters = cmdstring.rsplit(" ")
        print parameters
        cmdstring = parameters[0]
    else:
        parameters = [cmdstring,0,0,0,0]
        
    print "Got command " + cmdstring
    
    commandFromAdmin = 0
    
    if user in admins:
        commandFromAdmin = 1
        
    if cmdstring in freeCommandList or cmdstring in adminCommandList:
        print "Command " + cmdstring + " is valid."
        
        if cmdstring not in freeCommandList and cmdstring in adminCommandList:
            print "Command " + cmdstring + " is Admin only."
            if commandFromAdmin == 1:
                print "User " + user + " is Admin"
                return cmdstring
            else:
                print "User " + user + " is not admin. No command will be issued."
                return 0
        
        if cmdstring in freeCommandList and cmdstring not in adminCommandList:
            print "Command " + cmdstring + " is free for all users."
            return cmdstring
                
    else:
        print "Command is invalid."
        return 0
        
    

def RNG(number):
    randommin = random.randint(0,59)
    randomsec = random.randint(0,59)
    randomhour = random.randint(0,23)
    randomtime = randomhour*10000 + randommin*100 + randomsec + 9000000
    RNGs[number] = randomtime
    print str(number) + " : " + str(RNGs[number])
RNG(0)
RNG(1)

suggestions = open("suggestionbox.txt", "a")
with open("catfacts.txt", "r") as catfile:
    listcatfacts = [line.strip() for line in catfile]
#todo add exception when file isn't loaded
###This code was only run on one computer, so I never encountered these issues. I had never really planned on making this a large project, it was just something I did for fun and to annoy my friends.

def giveCatFact():
    print "Picking random Cat Fact"
    theCatFact = listcatfacts[random.randint(0,len(listcatfacts)-1)]
    print theCatFact
    return theCatFact

def sendCatFact(theCatFact):
    chat.SendMessage("Did you know?")
    chat.SendMessage(theCatFact)
    print theCatFact
    time.sleep(8)
    chat.SendMessage("Me neither!")


while 1:
    #time.sleep(0.05)
    for chat in skypeClient.BookmarkedChats:
        if chat.Name == '<CHAT GROUP ID GOES HERE>':
                    
            #check if message is the same as the new message
            if lastmessageid == chat.Messages[0].Id:
                newmessage = 0
            else:
                #print any new messages and prevent them from being printed again
                print chat.Messages[0].FromHandle + ' : ' + chat.Messages[0].Body
                lastmessage = chat.Messages[0].Body.encode( 'utf-8' )
                lastmsg = str(lastmessage).lower()
                # use lastmessage when case sensitive!
                # lastmsg is all lower case
				### naming conventions were not very good.
                lastmessageid = chat.Messages[0].Id
                lastmessagefrom = chat.Messages[0].FromHandle
                newmessage = 1
            #check any messages that may be direct commands
            if chat.Messages[0].Body.startswith("!") and newmessage == 1:
                commandstring = chat.Messages[0].Body.lstrip('!').lower()
                print "Command from " + lastmessagefrom + " : " + commandstring
                command = checkCommand(commandstring, lastmessagefrom.lower())
                commandok = 1
                
                # Regular time based events
                # they don't like the hourly clock anymore so let's kill that and never use it again
				
				### This drove everyone INSANE. I loved it. They didn't.
            
            if time.strftime('%H%M%S') == '000000':
                chat.SendMessage("It is now Midnight.")
                
                time.sleep(1)
            if time.strftime('%H%M%S') == '120000':
                chat.SendMessage("It's noon. Food time?")
                time.sleep(1)
            if time.strftime("%M%S") == '0000':
                print time.strftime("%H") + " hour"
                time.sleep(1)
                
                # RNG time based events
            
            if time.strftime("9%H%M%S") == str(RNGs[0]):
                thetime = time.strftime("%I:%M:%S %p")
                chat.SendMessage("The current time is "+thetime.lstrip('0'))
                time.sleep(1)
                RNG(0)
            if time.strftime("9%H%M%S") == str(RNGs[1]):
                giveCatFact()
                sendCatFact()
                time.sleep(1)
                RNG(1)
                # Conversational Events. Why was this taken out from Skypebot2?
				### ChrisBot went through a lot of changes.
            
            
            
        # Word driven events
            
            if newmessage == 1:
        # only do stuff to NEW messages
                if lastmsg == "hi" and lastmessageid.lower() == "tdog_63":
                    chat.SendMessage("Hi Tommmy.")
                if lastmsg.count('dota 2')>0:
                    chat.SendMessage("CSGO is the superior game ;D")
                    
            
            # Direct Commands that are FUN :D
            # Commands controlling fun are outside of the if statement so that they may be issued independently if fun is on or off
            if command == "fun":
                funAllowed = 1
                print "FUN ALLOWED"
            if command == "nofun":
                funAllowed = 0
                print "No fun"
            #print 'tick'

            if funAllowed == 1 and commandok == 1 or commandFromAdmin == 1:
                # fun is always ok if it's from an admin
                # if fun is allowed, direct commands are allowed to be issued.
				### Python doesn't have switch case, so this had to do.
                if command == "test": ### Python is weird, you can do this.
                    print "TEST TEST TEST" ### Debug commands are fun
                if command == "catfact": 
                    catFact = giveCatFact()
                    sendCatFact(catFact)
                if command == "omri":
                    chat.SendMessage("likes to bait us in csgo")
                if command == "chrisbot":
                    chat.SendMessage("ChrisBot is best bot")
                if command == "chris":
                    chat.SendMessage("is the greatest.")
                if command == "owen":
                    chat.SendMessage("is the debate lord")
                if command == "help":
                    chat.SendMessage("No help for you.")
                if command == "music":
                    chat.SendMessage('"Music" https://www.youtube.com/watch?v=X2WH8mHJnhM')
                if command == "clearsuggest":
                    suggestions.close()
                    suggestions = open("suggestionbox.txt", "w")
                    suggestions.write("File has been cleared.")
                    suggestions.write(time.strftime("%H:%M:%S %m/%d/%Y")+"\n")
                    suggestions.close()
                    suggestions = open("suggestionbox.txt", "a")
                    chat.SendMessage("Suggestion Box has been cleared.")
                if command == "suggest":
                    suggestions = open("suggestionbox.txt", "a")
                    suggestions.write(lastmessagefrom + " : " + lastmsg.lstrip("!suggest ") + "\n")
                    print lastmsg
                    chat.SendMessage("Your suggestion has been noted.")
                if command == "readsuggestions":
                    suggestions.close()
                    suggestions = open("suggestionbox.txt", "r")
                    chat.SendMessage(suggestions.read())
                    suggestions.close()
                    suggestions = open("suggestionbox.txt", "a")
                if command == "nuke":
                    chat.SendMessage("NME NUKE INCOMIN")
                    chat.SendMessage("https://www.youtube.com/watch?v=9qigsKZJ43k&html5=1")
                if command == "stopspam":
                    for x in range (0,9):
                        chat.SendMessage("STOP SPAMMING")
                if command == "spam":
                    for x in range (0,3):
                        chat.SendMessage("SPAM SPAM SPAM SPAM SPAMMILY SPAM! SPAMMILY SPAM!")
                if command == "bingo":
                    chat.SendMessage("https://www.youtube.com/watch?v=Sq1oO8kxyuE")
                    chat.SendMessage("BINGO BANGO BONGO BISH BASH BOSH")
                if command == "doge":
                    chat.SendMessage('░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░\n░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░\n░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░\n░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░\n░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░\n░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░\n░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░\n░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░\n░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░\n░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░\n▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░\n▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌\n▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░\n░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░\n░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░\n░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░\n░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░\n░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░\n░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░')
                if command == "usr":
                    chat.SendMessage(lastmessagefrom)
                    if commandFromAdmin == 1:
                        chat.SendMessage("User is admin")
                if command == "coinflip":
                    if random.randint(0,1) == 1:
                        chat.SendMessage("Heads")
                    else:
                        chat.SendMessage("Tails")
                if command == "randomnumber":
                    chat.SendMessage(random.randint(0,10))
                if command == "randompick":
                    chat.SendMessage("Picking a number 0-10")
                    time.sleep(10)
                    chat.SendMessage("Number is "+random.randint(0,10))
                if command == "commands":
                    chat.SendMessage("There's a lot of them.")
                    if commandFromAdmin == 1:
                        chat.SendMessage("Some admin-only commands are secret. You can use !fun !nofun !doge !catfact and !sleep")
                        print "Check out the code for all the commands!"
                if command == "sleep":
                    if parameters[1] != 0:
                        # make sure that the same message that issued the command with parameters is being stripped. There is a chance that skype lag could affect this
                        # TODO link this with message id's so that if skype lag happens and 2 people type the same command it doesn't take the parameter out of the newer
                        # command
                        
                        # TODO use float values and add exception if letters are following the commmand
                        # http://stackoverflow.com/questions/6941866/check-string-for-numbers-in-python
                        # do this for !cooldown as well
						
						
						### I encountered difficulties using the Skype4Py library, because it is based on the Skype4COM library, and that is depreciated.
						### As a result, documentation is difficult to find, and I think I encountered a few bugs.
                        sleepAmt = int(re.sub("[^0-9]", "", parameters[1]))
                    else:
                        sleepAmt = 180
                    chat.SendMessage("Sleeping for " + str(sleepAmt) + " seconds")
                    print "sleeping for " + str(sleepAmt)
                    time.sleep(sleepAmt)
                    print "done sleeping for " + str(sleepAmt)
                    chat.SendMessage("*Yawn* ChrisBot is feeling refreshed from a nice nap.")
                if command == "cooldown": ### The people in the skype chat would spam it, so I had to add a cooldown.
                    if lastmsg == "!cooldown":
                        chat.SendMessage("Cooldown is " + str(cmdCooldown))
                    if parameters[1] != 0:
                        # same reason as !sleep
                        cmdCooldown = int(re.sub("[^0-9]", "", parameters[1]))
                        chat.SendMessage("Cooldown is now " + str(cmdCooldown))
                    else:
                        cmdCooldown = 10        
            commandok = 0
            if command != 0:
                if commandFromAdmin == 0:
                    commandok = 0
                    time.sleep(cmdCooldown)
                else:
                    print 'comand from admin, no delay'
                    commandok = 1
                
                # no delay for admins :D
                
                        
