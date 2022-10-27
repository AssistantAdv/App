import pyautogui
from Resources.Scripts.Sound import speak
import ctypes
import speedtest
import time
from Resources.Scripts.Sound import takecom
import os

def but(query):

    if "enter" in query:
        speak("Okay! press entered")
        pyautogui.press("enter")

    elif "window" in query or "windows" in query:
        speak("Okay! press windows")
        pyautogui.press('win')

    elif "up" in query:
        speak("How many times of up's")
        while True:
            ti = int(takecom())
            if "none" in ti:
                speak("Please tell me how many up's")
            elif f"int{ti}" in ti:
                pyautogui.press('up', presses=ti)
                break

    elif "down" in query:
        speak("How many times of down")
        while True:
            ti = int(takecom())
            if "none" in ti:
                    speak("Please tell me how many down")
            else:
                pyautogui.press('down',presses=ti)
                break

    elif "left" in query:
        speak("How many times of left")
        while True:
            ti = int(takecom())
            if "none" in ti:
                speak("Please tell me how many left")
            else:
                pyautogui.press('left',presses=ti)
                break

    elif "right" in query:
        speak("How many times of right")
        while True:
            ti = int(takecom())
            if "none" in ti:
                speak("Please tell me how many right")
            else:
                pyautogui.press('right',presses=ti)
                break

    elif "tab" in query:
        speak("Okay! tab")
        pyautogui.press('tab')

    elif "copy" in query:
        speak("Copied")
        pyautogui.keyDown('ctrl')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')

    elif "cut" in query or "move" in query:
        speak("Moved")
        pyautogui.keyDown('ctrl')
        pyautogui.press('x')
        pyautogui.keyUp('ctrl')

    elif "save" in query:
        speak("Okay saved")
        pyautogui.keyDown('ctrl')
        pyautogui.press('s')
        pyautogui.keyUp('ctrl')

    elif "paste" in query:
        speak("Paste")
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')

def vol(query):
    
    if "increase" in query or "up" in query:
        try:
            query = query.replace("volume", "")
            query = query.replace("increase", "")
            query = query.replace("times", "")
            query = query.replace("time", "")
            query = int(query)
            speak(f"Okay {query} times volume increases")
            pyautogui.press('volumeup', interval=1, presses=query)
            speak("Done commander")
        except Exception:
            while True:
                dp = takecom()
                if "none" in dp:
                    speak("Please tell me how many volume increase")
                else:
                    dp = dp.replace("times", "")
                    dp = dp.replace("time", "")
                    dp = dp.replace("volume", "")
                    dp = dp.replace("increase", "")
                    try:
                        dp = int(dp)
                        speak(f"Okay {dp} times volume increases")
                        pyautogui.press('volumeup', interval=1, presses=dp)
                        speak("Done commander")
                        break
                    except Exception:
                        speak("There is not proper form")

    elif "decrease" in query or "down" in query:
        try:
            query = query.replace("volume", "")
            query = query.replace("decrease", "")
            query = query.replace("times", "")
            query = int(query)
            speak(f"Okay {query} times volume decrease")
            pyautogui.press('volumedown', interval=1, presses=query)
            speak("Done commander")
        except Exception:
            speak("How many times of volume decrease")
            while True:
                dp = takecom()
                if "none" in dp:
                    speak("Please tell me how many volume decrease")
                else:
                    dp = dp.replace("times", "")
                    dp = dp.replace("time", "")
                    dp = dp.replace("volume", "")
                    dp = dp.replace("decrease", "")
                    try:
                        dp = int(dp)
                        speak(f"Okay {dp} times volume decreases")
                        pyautogui.press('volumedown', interval=1, presses=dp)
                        speak("Done commander")
                        break
                    except Exception:
                        speak("There is not proper form")

    elif "mute" in query:
        speak("Muted")
        pyautogui.press('volumemute')

    elif "unmute" in query:
        pyautogui.press('volumemute')
        speak("Unmuted")

def win(query):

    if "lock the window" in query or "lock winodw" in query:
        speak("Okay sir windows locking")
        ctypes.windll.user32.LockWorkStation()

    elif "minimize the window" in query or "minimize window" in query or "minimise the window" in query or "minimise window" in query:
        speak("Okay minimizing")
        pyautogui.keyDown('win')
        pyautogui.press('m')
        pyautogui.keyUp('win')

    elif "maximize the window" in query or "maximize window" in query or "maximise the window" in query or "maximise window" in query:
        speak("Okay miximizing")
        pyautogui.keyDown('win')
        pyautogui.keyDown('shift')
        pyautogui.press('m')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('win')

def rest(query):

    if "restore left" in query:
        speak("Restoring left")
        pyautogui.keyDown('win')
        pyautogui.press('left')
        pyautogui.keyUp('win')

    elif "restore right" in query:
        speak("Restoring right")
        pyautogui.keyDown('win')
        pyautogui.press('right')
        pyautogui.keyUp('win')
    
    elif "restore up" in query:
        speak("Restoring up")
        pyautogui.keyDown('win')
        pyautogui.press('up')
        pyautogui.keyUp('win')

    elif "restore down" in query:
        speak("Restoring down")
        pyautogui.keyDown('win')
        pyautogui.press('down')
        pyautogui.keyUp('win')

def oth(query):

    if "antonym" in query or "synonym" in query or "meaning" in query:
        from PyDictionary import PyDictionary as Diction
        speak("Tell me the problem")
        if "meaning" in query:
            op = query.replace("what is the", "")
            op = op.replace("meaning", "")
            op = op.replace("of", "")
            result = Diction.meaning(op)
            speak(f"The meaning of {op} is {result}")

        elif "synonym" in query:
            op = query.replace("what is the", "")
            op = op.replace("synonym", "")
            op = op.replace("of", "")
            result = Diction.synonym(op)
            speak(f"The synonym of {op} is {result}")

        elif "antonym" in query:
            op = query.replace("what is the", "")
            op = op.replace("antonym", "")
            op = op.replace("of", "")
            result = Diction.antonym(op)
            speak(f"The antonym of {op} is {result}")

    elif "translate" in query or "translator" in query:
        from Resources.Scripts.Trans import Translate
        speak("Tell Me The Line!")
        line = takecom()
        Translate(line)

    elif "blutooth on" in query:
        from Resources.Scripts.System import onoff
        onoff("on")

    elif "read pdf" in query:
        from Resources.Scripts.Wish import pdf
        pdf()

    elif "hide" in query or "unhide" in query or "invisible" in query or "visible" in query:
        from Resources.Scripts.Trans import hide
        hide()

    elif "internet speed" in query or "network speed" in query:
        if "internet speed" in query:
            speak("Please wait sir, fetching the internet speed")
        elif "network speed" in query:
            speak("Please wait sir, fetching the network speed")
        st = speedtest.Speedtest()
        dl = st.download()
        up = st.upload()
        speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

    elif "internet information" in query or "network information" in query:
        try:
            sp = os.system('cmd /k "speedtest"')
            speak(sp)
        except:
            speak("There is no internet connection")

    elif "what's up" in query or 'tum kaise ho' in query:
        import random
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy', 'I am okay']
        ans_q = random.choice(stMsgs)
        speak(ans_q)
        ans_take_from_user_how_are_you = takecom()
        speak("How are you sir")
        while True:
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okay' in ans_take_from_user_how_are_you:
                speak('Thats great')
                break
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you or "i am not okay" in ans_take_from_user_how_are_you:
                speak('Oh sorry..')
                break
            elif "none" in ans_take_from_user_how_are_you:
                speak("Please sir tell me how are you")

    elif "also good" in query or "i am also good" in query:
        speak("That's great to here from you.")

    elif 'video downloader' in query:
        from Resources.Scripts.Video_Downloader import downloader
        downloader()

    elif "your name" in query or "sweat name" in query:
        speak("Thanks for Asking my name my self ! Alexa")

    elif "you feeling" in query:
        speak("Feeling Very sweet after meeting with you")

    elif 'remind that' in query or "remember that" in query:
        remembermsg = query.replace('remind that', '')
        remembermsg = remembermsg.replace("Alexa", "")
        speak(f"Ok i will remember :{remembermsg}")
        remember = open('data.txt','w')
        remember.write(remembermsg)
        remember.close()

    elif 'what remember' in query or "what remind" in query:
        remember = open('data.txt', 'r')
        speak(f"You told me {remember.read()}")

    elif "are you intelligent" in query or "you are intelligent" in query:
        speak("No, you are intelligent")

    elif "shutdown" in query:
        speak("Are you sure to pc shutdown")
        while True:
            tk = takecom()
            if "yes" in tk or "sure" in tk:
                speak("Okay, Sir i am now shutting down")
                os.system("shutdown /s /t 5")
            elif "none" in tk:
                speak("Sir, Are you sure to shutting down")
            elif "no" in tk:
                speak("Okay, I am not shutting down")
                break
 
    elif "restart" in query:
        speak("Are you sure to i am restart")
        while True:
            tk = takecom()
            if "yes" in tk or "sure" in tk:
                speak("Okay, Sir i am restarting now")
                os.system("shutdown /r /t 5")
            elif "none" in tk:
                speak("Sir, Are you sure to i am restarting")
            elif "no" in tk:
                speak("Okay I am not restarting")
                break

    elif "sleep" in query:
        speak("Are you sure to i am sleep")
        while True:
            tk = takecom()
            if "yes" in tk or "sure" in tk:
                speak("Okay, Sir i am sleeping now")
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                break
            elif "no" in tk:
                speak("Okay, I am not going sleep")
                break
            else:
                speak("Sir, Are you sure to sleep")

    elif "space news" in query:
        from Resources.Scripts.Nasa import Nasanews
        speak("Tell me year")
        yy = int(takecom())
        speak("Tell me month")
        mm = int(takecom())
        speak("Tell me date")
        dd = int(takecom())
        Date = f"{yy}-{mm}-{dd}"
        Nasanews(Date)

    elif "google information" in query:
        import requests
        from bs4 import BeautifulSoup
        speak("What should i search on google")
        while True:
            sear = takecom()
            if "none" in sear:
                speak("Please tell me what should i search")

            elif "exit" in sear:
                speak("Exiting...")
                break

            else:
                sear = sear.replace("none", "")
                sear = sear.replace("exit", "")
                url = f"https://www.google.com/search?q={sear}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(temp)
                break

    elif "tell me" in query:
        query = query.replace("tell me", "")
        query = query.replace("the", "")
        import wolframalpha
        app = wolframalpha.Client("EU583K-7HU7A3UKVU")
        res = app.query(query)
        speak(next(res.results).text)

    elif "my location" in query:
        from Resources.Scripts.Location import loc
        loc()

    elif "instagram profile" in query:
        from Resources.Scripts.Insta import insta
        insta()

    elif "battery" in query or "charging" in query:
        from Resources.Scripts.Battery import bat
        bat()

    elif "message" in query or "send" in query:
        from Resources.Scripts.Message import msg
        msg()

    elif "jokes" in query or "joke" in query:
        from Resources.Scripts.Jokes import joke
        joke()

    elif "shayari" in query:
        from Resources.Scripts.Jokes import shay
        shay()

    elif "alarm" in query:
        from Resources.Scripts.Alarm import alarm
        speak("Tell me time of set alarm")
        while True:

            try:
                tt = takecom()
                if "exit" in tt or "no set" in tt:
                    speak("Exiting...")
                    break
                
                elif "none" in tt:
                    speak("Please sir tell me the time of set alarm")

                else:
                    tt = tt.replace("exit", "")
                    tt = tt.replace("none", "")
                    tt = tt.replace("no", "")
                    tt = tt.replace("set", "")
                    tt = tt.replace("Alexa", "")
                    tt = tt.replace(".","")
                    tt = tt.replace("alarm", "")
                    tt = tt.replace("to", "")
                    tt = tt.upper()
                    alarm(tt)
                    break
            
            except Exception:
                speak("Please tell me valid timing")

    elif "type" in query:
        speak("What type please tell me")
        while True:
            fm = takecom()
            if "none" in fm:
                speak("Please sir tell me what shoult i type")
            elif "exit" in fm or "stop" in fm:
                if "stop" in fm:
                    speak("Stop Typing...")
                    break
                elif "exit" in query:
                    speak("Exiting...")
            else:
                pyautogui.typewrite(f"{fm}")

    elif "caps lock" in query:
        speak(query)
        pyautogui.press('caps lock')

    elif "screenshot" in query:
        speak("Sir, please tell me the name for this screenshot file")
        while True:
            name = takecom()
            if "none" in name:
                speak("Please sir tell me name of screenshot file")
            else:
                speak("Please sir hold the screen for few seconds, i am taking screenshot")
                img = pyautogui.screenshot()
                img.save(f"C:\\Users\\HP\\OneDrive\\Desktop\\AI\\Alexa\\Database\\Screenshot\\{name}.png")
                speak("I am done sir, the screenshot is saved in our database folder. now i am ready for next command")
                break      

    elif "write" in query:
        from Resources.Scripts.Auto import typeing
        typeing(query)

    elif "repeat" in query:
        query = query.replace("repeat", "")
        speak(f"{query}")

    elif "photos" in query or "photos" in query:
        from Resources.Scripts.Search import search
        search(query)

    elif "what happen" in query or "kya hua" in query:
        speak("No No! Nothing! kuch nahi hua")

    elif "my words repeat" in query:
        speak("Speak sir")
        fg = takecom()
        speak(f"You said : {fg}")

    elif "ip address" in query or "my ip address" in query:
        import requests
        ip = requests.get('https://api.ipify.org').text
        speak(f"Your IP address is {ip}")
            
    elif "call" in query:
        speak("Okay! i am calling.....")

        from twilio.rest import Client

        account_sid = 'ACf3b1435ba5f416079d2819e09cfc90ae'
        auth_token = '8fa4435206dea378e83afb9923f5212c'

        client = Client(account_sid, auth_token)

        message = client.calls \
            .create(
                twiml='<Response><Say>This is the second testing message from Alexa side. and i am software engineer how are you and who are you..</Say></Response>',
                from_='+17242643047',
                to='+919049957250'
            )

        print(message.sid)

    elif "get info" in query or "get information" in query:
        import pywhatkit as kit
        speak("Tell me topic get information")
        while True:
            ti = takecom()
            if "none" in ti:
                speak("Please tell me topic information")
            else:
                try:
                    hit = kit.info(ti, lines=10)
                    speak(hit.summary)
                    print("\nSuccessful search")
                except Exception as e:
                    print("An Unknown Error Occured")
                    break

    elif 'make you' in query or 'created you' in query or 'develop you' in query or "born you" in query:
        speak("For your information Prashik likhar Created me ! I give Lot of Thannks to Him")

    elif "time" in query:
        import datetime
        dt = datetime.datetime.now()
        speak('%s:%s:%s' % (dt.hour, dt.minute, dt.second))

    elif "date" in query:
        import datetime
        dt = datetime.datetime.now()
        speak('%s:%s:%s' % (dt.day, dt.month, dt.year))

    elif "who your developer" in query:
        speak("I am develope prashik sir")

    elif "who are you" in query or "about you" in query or "your details" in query:
        import wikipedia
        speak("I am Alexa an A I based computer program but I can help you lot like a your close friend, I promise you, Simple try me to give simple command, like playing music or video from your directory I also play video and song from web or online, I can also entain you I so think you Understand me, ok Lets Start ")
        speak("Many more information about me yes or no")
        while True:
            hm = takecom()
            if "yes" in hm :
                jk = "Artificial Intelligence"
                results = wikipedia.summary(jk, sentences = 10)
                speak("Okay! more information")
                speak(results)
            
            elif "none" in hm:
                speak("Please sir tell me yes or no")
            
            elif "no" in hm :
                speak("Okay! no more information")
                break
        
    elif "password" in query or "unlock" in query:
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite("2021")
        pyautogui.press('enter')
    
    elif "what is your name" in query:
        speak("My name is Alexa")

    elif "morning" in query or "afternoon" in query or "evening" in query:
        from Resources.Scripts.Wish import wish
        wish()

    elif "i am fine" in query:
        speak("That's great")

    elif "full screen" in query:
        speak("Full screen in")
        pyautogui.press('f11')

    elif "out full screen" in query:
        speak("Full screen out")
        pyautogui.press('f11')

    elif "select all" in query or "all select" in query:
        speak("All selected")
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.keyUp('ctrl')

    elif "copy" in query or "cut" in query or "save" in query or "move" in query or "paste" in query:
        from Resources.Scripts.Other import but
        but(query)

    elif "word find" in query:
        pyautogui.keyDown('ctrl')
        pyautogui.press('f')
        pyautogui.keyUp('ctrl')
        speak("What i find tell me")
        while True:
            rf = takecom()
            if "none" in rf:
                speak("Please tell me sir what i find")
            else:
                pyautogui.typewrite(f"{rf}")
                break

    elif "task view" in query or "pass view" in query:
        speak("Task view")
        pyautogui.keyDown('winriqueryt')
        pyautogui.keyDown('tab')
        pyautogui.keyUp('winriqueryt')
        pyautogui.keyUp('tab')
        time.sleep(3)
        pyautogui.press('left')
        pyautogui.press('Enter')

    elif "space photos" in query:
        from Resources.Scripts.Nasa import Images
        speak("How many photos")
        pt = int(takecom())
        Images(pt)

    elif "astro" in query or "asteroid" in query:
        from Resources.Scripts.Nasa import Astro
        speak("1 : Set as default")
        speak("2 : Set date")
        while True:
            tk = takecom
            if "set date" in tk or "2" in tk:
                speak("Tell me start year")
                break
            else:
                start = "2020-01-01"
                end = "2020-01-05"
                Astro(start,end)
                break

    elif "intelligent mode activate" in query or "activate intelligent mode" in query:
        from Resources.Scripts.Intel import lit
        speak("Intelligent mode activated")
        lit()

    elif "tell me news" in query or "tell me the news" in query or "tell me the today's news" in query:
        from Resources.Scripts.News import news
        news()

    elif "desktop" in query:
        pyautogui.keyDown('win')
        pyautogui.press('d')
        pyautogui.keyUp('win')
        speak("Run on desktop")

    elif "switch" in query or "change" in query:
        speak("Changing...")
        pyautogui.keyDown('alt')
        pyautogui.press('esc')
        pyautogui.keyUp('alt')

    elif "thank you" in query or "thanks" in query:
        speak("It's my pleasure sir.")

    else:
        from Resources.Scripts.ChatBot import ChatterBot
        ChatterBot(query)    

    