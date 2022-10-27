import random
from Resources.Scripts.Sound import speak

Hello = ('hello','hey','hii','hi')
reply_Hello = ('Hello Sir , I Am Alexa.',
            "Hey, What's Up ?",
            "Hey, How Are You ?",
            "Hello Sir , Nice To Meet You Again.",
            "Of Course Sir , Hello.")

Bye = ('bye','exit','sleep')
reply_bye = ('Bye Sir.',
            "It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ('how','fine')
reply_how = ('I Am Fine.',
            "Excellent.",
            "Moj Ho rhi Hai.",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks')
reply_nice = ('Thanks.',
            "Ohh , It's Okay.",
            "Thanks To You.")

Functions = ['functions','abilities','what','features']
reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'I Can Call Your G.F.',
            'I Can Message Your Mom That You Are Not Studing.',
            'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry, I Can't Understand",
                "Sorry , I Can't Do That .",
                "Sorry , That's Above Me.")

def ChatterBot(Text):
    Text = str(Text)
    for word in Text.split():
        
        if word in Hello:
            reply = random.choice(reply_Hello)
            speak(reply)
            return reply

        elif word in Bye:
            reply = random.choice(reply_bye)
            speak(reply)
            return reply

        elif word in How_Are_You:
            reply_ = random.choice(reply_how)
            speak(reply_)
            return reply_

        elif word in Functions:
            reply___ = random.choice(reply_Functions)
            speak(reply___)
            return reply___

        else:
            ret = random.choice(sorry_reply)
            speak(ret)
            return ret
