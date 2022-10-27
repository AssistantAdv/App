from Resources.Scripts.Sound import say, takecom
import random
import os
import requests
from bs4 import BeautifulSoup
import pyautogui
from twilio.rest import Client
import pywhatkit as kit
import wikipedia
import datetime
import time
import wolframalpha
from gtts import gTTS
from playsound import playsound
import ctypes
import webbrowser
import instaloader
from googletrans import Translator
from tkinter import Tk, Label, Entry, StringVar, Button
import asyncio
import psutil
from pywikihow import search_wikihow
import PyPDF2
from pytube import YouTube 

class All():

    def all(query):
        if "translate" in query or "translator" in query:
            say("Tell Me The Line!")
            line = takecom()
            All.Translate(line)

        elif "blutooth on" in query:
            All.onoff("on")

        elif "read pdf" in query:
            All.pdf()

        elif "hide" in query or "unhide" in query or "invisible" in query or "visible" in query:
            All.hide()

        elif "ok" in query or "okay" in query:
            say("What okay")

        elif "what's up" in query or 'tum kaise ho' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy', 'I am okay']
            ans_q = random.choice(stMsgs)
            say(ans_q)
            ans_take_from_user_how_are_you = takecom()
            say("How are you sir")
            while True:
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okay' in ans_take_from_user_how_are_you:
                    say('Thats great')
                    break
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you or "i am not okay" in ans_take_from_user_how_are_you:
                    say('Oh sorry..')
                    break
                elif "none" in ans_take_from_user_how_are_you:
                    say("Please sir tell me how are you")

        elif "also good" in query or "i am also good" in query:
            say("That's great to here from you.")

        elif 'video downloader' in query:
            All.downloader()

        elif "your name" in query or "sweat name" in query:
            say("Thanks for Asking my name my self !")

        elif "you feeling" in query:
            say("Feeling Very sweet after meeting with you")

        elif 'remind that' in query or "remember that" in query:
            remembermsg = query.replace('remind that', '')
            remembermsg = remembermsg.replace("Alexa", "")
            say(f"Ok i will remember :{remembermsg}")
            remember = open('Resources/Startups/data.txt','w')
            remember.write(remembermsg)
            remember.close()

        elif 'what remember' in query or "what remind" in query:
            remember = open('Resources/Startups/data.txt', 'r')
            say(f"You told me {remember.read()}")

        elif "are you intelligent" in query or "you are intelligent" in query:
            say("No, you are intelligent")

        elif "shutdown" in query:
            say("Are you sure to pc shutdown")
            while True:
                tk = takecom()
                if "yes" in tk or "sure" in tk:
                    say("Okay, Sir i am now shutting down")
                    os.system("shutdown /s /t 5")
                elif "none" in tk:
                    say("Sir, Are you sure to shutting down")
                elif "no" in tk:
                    say("Okay, I am not shutting down")
                    break
    
        elif "restart" in query:
            say("Are you sure to i am restart")
            while True:
                tk = takecom()
                if "yes" in tk or "sure" in tk:
                    say("Okay, Sir i am restarting now")
                    os.system("shutdown /r /t 5")
                elif "none" in tk:
                    say("Sir, Are you sure to i am restarting")
                elif "no" in tk:
                    say("Okay I am not restarting")
                    break

        elif "sleep" in query:
            say("Are you sure to i am sleep")
            while True:
                tk = takecom()
                if "yes" in tk or "sure" in tk:
                    say("Okay, Sir i am sleeping now")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                    break
                elif "no" in tk:
                    say("Okay, I am not going sleep")
                    break
                else:
                    say("Sir, Are you sure to sleep")

        elif "space news" in query:
            say("Tell me year")
            yy = int(takecom())
            say("Tell me month")
            mm = int(takecom())
            say("Tell me date")
            dd = int(takecom())
            Date = f"{yy}-{mm}-{dd}"
            All.Nasanews(Date)

        elif "google information" in query:
            say("What should i search on google")
            while True:
                sear = takecom()
                if "none" in sear:
                    say("Please tell me what should i search")

                elif "exit" in sear:
                    say("Exiting...")
                    break

                else:
                    sear = sear.replace("none", "")
                    sear = sear.replace("exit", "")
                    url = f"https://www.google.com/search?q={sear}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    say(temp)
                    break

        elif "my location" in query:
            All.loc()

        elif "instagram profile" in query:
            All.insta()

        elif "battery" in query or "charging" in query:
            All.bat()

        elif "message" in query or "send" in query:
            All.msg()

        elif "jokes" in query or "joke" in query:
            All.joke()

        elif "shayari" in query:
            All.shay()

        elif "alarm" in query:
            say("Tell me time of set alarm")
            while True:

                try:
                    tt = takecom()
                    if "exit" in tt or "no set" in tt:
                        say("Exiting...")
                        break
                    
                    elif "none" in tt:
                        say("Please sir tell me the time of set alarm")

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
                        All.alarm(tt)
                        break
                
                except:
                    say("Please tell me valid timing")

        elif "type" in query or "typing" in query:
            say("What type please tell me")
            while True:
                fm = takecom()
                if "none" in fm:
                    say("Please sir tell me what shoult i type")
                elif "exit" in fm or "stop" in fm:
                    if "stop" in fm:
                        say("Stop Typing...")
                        break
                    elif "exit" in query:
                        say("Exiting...")
                else:
                    pyautogui.typewrite(f"{fm}")

        elif "caps lock" in query:
            say(query)
            pyautogui.press('caps lock')

        elif "screenshot" in query:
            say("Sir, please tell me the name for this screenshot file")
            while True:
                name = takecom()
                if "none" in name:
                    say("Please sir tell me name of screenshot file")
                else:
                    say("Please sir hold the screen for few seconds, i am taking screenshot")
                    img = pyautogui.screenshot()
                    img.save(f"Resources/Images/{name}.png")
                    say("I am done sir, the screenshot is saved in our database folder. now i am ready for next command")
                    break      

        elif "write" in query:
            All.typing(query)

        elif "repeat" in query:
            query = query.replace("repeat", "")
            say(f"{query}")

        elif "what happen" in query:
            say("No No! Nothing!")

        elif "my words repeat" in query:
            say("say sir")
            fg = takecom()
            say(f"You said : {fg}")

        elif "ip address" in query or "my ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            say(f"Your IP address is {ip}")
                
        elif "call" in query:
            say("Okay! i am calling.....")

            account_sid = 'ACf3b1435ba5f416079d2819e09cfc90ae'
            auth_token = '8fa4435206dea378e83afb9923f5212c'

            client = Client(account_sid, auth_token)

            message = client.calls \
                .create(
                    twiml='<Response><Say>This is the second testing message from Alexa side. and i am software engineer how are you and who are you..</Say></Response>',
                    from_='+17242643047',
                    to='+918329863637'
                )

            print(message.sid)

        elif "get info" in query or "get information" in query:
            say("Tell me topic get information")
            while True:
                ti = takecom()
                if "none" in ti:
                    say("Please tell me topic information")
                else:
                    try:
                        hit = kit.info(ti, lines=10)
                        say(hit.summary)
                        print("\nSuccessful search")
                    except Exception as e:
                        print("An Unknown Error Occured")
                        break

        elif 'make you' in query or 'created you' in query or 'develop you' in query or "born you" in query:
            say("For your information Prashik likhar Created me ! I give Lot of Thannks to Him")

        elif "time" in query:
            dt = datetime.datetime.now()
            say('%s:%s:%s' % (dt.hour, dt.minute, dt.second))

        elif "date" in query:
            dt = datetime.datetime.now()
            say('%s:%s:%s' % (dt.day, dt.month, dt.year))

        elif "who your developer" in query:
            say("I am develope prashik sir")

        elif "who are you" in query or "about you" in query or "your details" in query:
            say("I am Alexa an A I based computer program but I can help you lot like a your close friend, I promise you, Simple try me to give simple command, like playing music or video from your directory I also play video and song from web or online, I can also entain you I so think you Understand me, ok Lets Start ")
            say("Many more information about me yes or no")
            while True:
                hm = takecom()
                if "yes" in hm :
                    jk = "Artificial Intelligence"
                    results = wikipedia.summary(jk, sentences = 10)
                    say("Okay! more information")
                    say(results)
                
                else:
                    say("Okay! no more information")
                    break
                    
        elif "what is your name" in query:
            say("My name is Alexa")

        elif "morning" in query or "afternoon" in query or "evening" in query:
            All.wish()

        elif "i am fine" in query:
            say("That's great")

        elif "full screen" in query:
            say("Full screen in")
            pyautogui.press('f11')

        elif "out full screen" in query:
            say("Full screen out")
            pyautogui.press('f11')

        elif "select all" in query or "all select" in query:
            say("All selected")
            pyautogui.keyDown('ctrl')
            pyautogui.press('a')
            pyautogui.keyUp('ctrl')

        elif "copy" in query or "cut" in query or "save" in query or "move" in query or "paste" in query:
            All.but(query)

        elif "word find" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('f')
            pyautogui.keyUp('ctrl')
            say("What i find tell me")
            while True:
                rf = takecom()
                if "none" in rf:
                    say("Please tell me sir what i find")
                else:
                    pyautogui.typewrite(f"{rf}")
                    break

        elif "task view" in query or "pass view" in query:
            say("Task view")
            pyautogui.keyDown('winriqueryt')
            pyautogui.keyDown('tab')
            pyautogui.keyUp('winriqueryt')
            pyautogui.keyUp('tab')
            time.sleep(3)
            pyautogui.press('left')
            pyautogui.press('Enter')

        elif "space photos" in query:
            say("How many photos")
            pt = int(takecom())
            All.Nasa_Images(pt)

        elif "astro" in query or "asteroid" in query:
            say("1 : Set as default")
            say("2 : Set date")
            while True:
                tk = takecom
                if "set date" in tk or "2" in tk:
                    say("Tell me start year")
                    break
                else:
                    start = "2020-01-01"
                    end = "2020-01-05"
                    All.Astro(start,end)
                    break

        elif "intelligent mode activate" in query or "activate intelligent mode" in query:
            say("Intelligent mode activated")
            All.lit()

        elif "tell me news" in query or "tell me the news" in query or "tell me the today's news" in query:
            All.news()

        elif "desktop" in query:
            pyautogui.keyDown('win')
            pyautogui.press('d')
            pyautogui.keyUp('win')
            say("Run on desktop")

        elif "switch" in query or "change" in query:
            say("Changing...")
            pyautogui.keyDown('alt')
            pyautogui.press('esc')
            pyautogui.keyUp('alt')

        elif "volume" in query:
            query = query.replace("volume", "")
            All.vol(query)

        elif "windows" in query or "window" in query:
            query = query.replace("windows", "")
            query = query.replace("window", "")
            All.win(query)

        elif "restore" in query:
            query = query.replace("restore", "")
            All.rest(query)

        elif "mute" in query or "unmute" in query:
            All.vol(query)

        elif "tell me" in query:
            query = query.replace("tell me", "")
            query = query.replace("the", "")
            app = wolframalpha.Client("EU583K-7HU7A3UKVU")
            res = app.query(query)
            say(next(res.results).text)

        elif "thank you" in query or "thanks" in query:
            say("It's my pleasure sir.")

        else:
            All.ChatterBot(query)    

    def wish():
        hour = int(datetime.datetime.now().hour)
        dt = datetime.datetime.now()
        if hour>=0 and hour<12:
            say("Good morning sir")
        elif hour>=12 and hour<18:
            say("Good afternoon sir")
        else:
            say("Good evening sir")
        say(dt.strftime("time %H:%M"))
        say("Would like to hear today's latest news.")
        say("Tell me yes or no")
        while True:
            new = takecom()
            if "yes" in new:
                All.news()
                say("This was some of today's latest news.")
                break
            elif "no" in new:
                say("Ok will not tell today's latest news.")
                break
            elif "none" in new:
                say("Please sir tell me yes or no")
            else:
                say("Sorry sir but I cant understand, try again")
        say("Please tell me how can i help you sir.")

    def vol(query):
        
        if "increase" in query or "up" in query:
            try:
                query = query.replace("volume", "")
                query = query.replace("increase", "")
                query = query.replace("times", "")
                query = query.replace("time", "")
                query = int(query)
                say(f"Okay {query} times volume increases")
                pyautogui.press('volumeup', presses=query)
                say("Done commander")
            except Exception:
                say("How many times of volume increase")
                while True:
                    dp = takecom()
                    if "none" in dp:
                        say("Please tell me how many volume increase")
                    else:
                        dp = dp.replace("times", "")
                        dp = dp.replace("time", "")
                        dp = dp.replace("volume", "")
                        dp = dp.replace("increase", "")
                        try:
                            dp = int(dp)
                            say(f"Okay {dp} times volume increases")
                            pyautogui.press('volumeup', presses=dp)
                            say("Done commander")
                            break
                        except Exception:
                            say("There is not proper form")

        elif "decrease" in query or "down" in query:
            try:
                query = query.replace("volume", "")
                query = query.replace("decrease", "")
                query = query.replace("times", "")
                query = int(query)
                say(f"Okay {query} times volume decrease")
                pyautogui.press('volumedown', presses=query)
                say("Done commander")
            except Exception:
                say("How many times of volume decrease")
                while True:
                    dp = takecom()
                    if "none" in dp:
                        say("Please tell me how many volume decrease")
                    else:
                        dp = dp.replace("times", "")
                        dp = dp.replace("time", "")
                        dp = dp.replace("volume", "")
                        dp = dp.replace("decrease", "")
                        try:
                            dp = int(dp)
                            say(f"Okay {dp} times volume decreases")
                            pyautogui.press('volumedown', presses=dp)
                            say("Done commander")
                            break
                        except Exception:
                            say("There is not proper form")

        elif "mute" in query:
            say("Muted")
            pyautogui.press('volumemute')

        elif "unmute" in query:
            pyautogui.press('volumemute')
            say("Unmuted")

    def rest(query):

        if "restore left" in query:
            say("Restoring left")
            pyautogui.keyDown('win')
            pyautogui.press('left')
            pyautogui.keyUp('win')

        elif "restore right" in query:
            say("Restoring right")
            pyautogui.keyDown('win')
            pyautogui.press('right')
            pyautogui.keyUp('win')
        
        elif "restore up" in query:
            say("Restoring up")
            pyautogui.keyDown('win')
            pyautogui.press('up')
            pyautogui.keyUp('win')

        elif "restore down" in query:
            say("Restoring down")
            pyautogui.keyDown('win')
            pyautogui.press('down')
            pyautogui.keyUp('win')

    def msg():
        say("Sir what should i send a message")
        while True:
            msz = takecom()
            if "none" in msz:
                say("Please tell me what should i send message")
            elif "exit" in msz:
                say("Exiting...")
                break
            else:
                from twilio.rest import Client

                account_sid = 'ACf3b1435ba5f416079d2819e09cfc90ae'
                auth_token = '8fa4435206dea378e83afb9923f5212c'

                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body=msz,
                        from_='+17242643047',
                        to='+919049957250'
                    )

                print(message.sid)
                break

    def joke():
        jokes = (
            
            " ज़रुरत से ज्यादा भगवान को याद मत किया करो क्योंकि किसी दिन भगवान ने याद कर लिया तो.?? लेने के देने पड़ जायेंगे । ",

            " काम ऐसे करो कि लोग आपको. किसी दूसरे काम के लिए बोलें ही नहीं ",

            " आज के जमाने में सत्संग उसी संत का बढ़िया रहता है, जिसके पंडाल में गर्म पोहा, समोसा जलेबी और अदरक वाली चाय मिले। वरना ज्ञान तो अब ऑनलाइन उपलब्ध है । ",

            " जिस पुरुष ने आज के समय में बीवी, नौकरी और स्मार्टफोन को सम्भाल लिया हो, वह पुरुष नहीं महापुरुष कहलाता है ",

            " आज सबसे बड़ी कुर्बानी वह होती है, जब हम अपना फोन चार्जिंग से निकाल कर किसी और का फोन लगा दें । ",

            " आप कितने ही अच्छे काम कर लें, लेकिन लोग उसे ही याद करते हैं, जो उधार लेकर मरा हो । ",

            " आजकल माता-पिता को बस दो ही चिंताएं हैं… इंटरनेट पर उनका बेटा क्या डाउनलोड कर रहा है…. और… बेटी क्या अपलोड कर रही है । ",

            " English के अलावा हिंदी में भी कुछ शब्द Silent होते हैं। जैसे की अगर ध्यान दिया हो तो… , जब कोई दुकानदार भाव करते समय कहता है कि आपको ज्यादा नहीं लगाएंगे तो इसमें.. “चूना” शब्द Silent होता है. ",
                    
            " एक लड़की एक लड़के के साथ बैठी थी, दूसरे दिन दूसरे लड़के के साथ बैठी थी, तीसरे दिन तीसरे लड़के के साथ बैठी थी, इस कहानी से तुम्हें क्या शिक्षा मिलती है? लड़के बदल जाते हैं पर लड़कियां नहीं ",

            " महिला बोली डॉक्टर साहब, मेरे पति नींद में बातें करने लगे हैं! क्या करूँ? डॉक्टर :- उन्हें दिन में बोलने का मौका दीजिए! ",

            " रक्षाबंधन पर लड़कियां किसी को भी भाई बना सकती हैं तो फिर करवाचौथ पर पति क्यों नही बनाती..? हमे इंसाफ चाहिए… *अब ये अफवाह कौन उड़ाया हैं कि * *मायावती रक्षाबंधन पर महागठबंधन के सभी नेताओ को ",

            " Sanskrit Teacher बोली, What is the meaning of तमसो मा ज्योर्तिगमय. Student बोला तू सो जा माँ, मैं ज्योति के घर जा रहा हुँ । ",

            " मरीज बोला, डॉक्टर साहब, मेरी दाई टांग में बहोत दर्द रहेता है. डॉक्टर बोला, ये तो उम्र का तकाजा है. मरीज बोला, लेकिन मेरी बाई टांग की भी तो उम्र उतनी ही है, फिर दाई टांग में ही तकलिफ क्यों ?? ",

            " जज बोला अच्छा, तो इस आदमी ने तुम्हें कौन-कौन सी गालियाँ दी. आदमी बोला जज साहब… वो सब गालियाँ शरीफों के सामने देने लायक नहीं है. वकील बोला अच्छा, तो हम सब यहाँ से चले जाते है. तूम जज को सुना दो. ",

            " Train में सांता का 100 रूपये गुम हो गये। तभी 1 मुसलमान बोला “या अल्लाह बिसमिल्लाह” सांता तुझे बीस मिला तो साला बाकी का 80 किसको मिला ",

            " कौन कहता है कि सिर्फ मोहब्बत में ही दर्द होता है । कमबख्त अभी दरवाजे में ऊंगली डालो तो पता चले क्या होता है ",

            "सान्ता ने बन्ता को थप्पड मार दिया… बन्ता बोला “ये तुने मजाक में मारा या #सच में मारा ?” सान्ता बोला “सच में मारा” बन्ता बोला “तो ठीक है, मुझे मजाक बिलकुल पसंद नहीं है”",

            '''सान्ता English के पेपर translation की वजह से फेल हो गया
                प्रश्न थे
                1. मैं एक आम आदमी हुँ ।
                सान्ता ने लिखा I am a Mango Man.
                2. मुझे इंग्लिस आती है ।
                सान्ता ने लिखा English Come to me
                3. मेरा तालुक हरिपुर हजारा से है ।
                सान्ता ने लिखा I belong to Greenpur Thousanda.
                4. सड़क पर गोलियाँ चल रही थी ।
                सान्ता ने लिखा Tablets are walking on the Road.''')

        jok = random.choice(jokes)
        tts = gTTS(text=jok, lang="hi", slow=False)
        filename = "Resources/Sound/my.mp3"
        tts.save(filename)
        playsound(filename)
        playsound("Resources/Sound/funny.mp3")
        os.remove(filename)

    def win(query):

        if "lock" in query:
            say("Okay sir windows locking")
            ctypes.windll.user32.LockWorkStation()

        elif "minimize" in query or "minimise" in query:
            say("Okay minimizing")
            pyautogui.keyDown('win')
            pyautogui.press('m')
            pyautogui.keyUp('win')

        elif "maximize" in query or "maximise" in query:
            say("Okay miximizing")
            pyautogui.keyDown('win')
            pyautogui.keyDown('shift')
            pyautogui.press('m')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('win')

    def search(query, cm):
    
        if "youtube" in query:
            webbrowser.open(f"http://www.youtube.com/results?search_query={cm}")
        
        elif "facebook" in query:
            webbrowser.open(f"https://www.facebook.com/search/top?q={cm}")
                
        elif "amazon" in query:
            webbrowser.open(f"https://www.amazon.com/s?k={cm}&ref=nb_sb_noss_2")

        elif "flipkart" in query:
            webbrowser.open(f"https://www.flipkart.com/search?q={cm}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

        elif "snapdeal" in query:
            webbrowser.open(f"https://www.snapdeal.com/search?keyword={cm}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")

        elif "ebay" in query:
            webbrowser.open(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={cm}&_sacat=0")

        elif "yahoo" in query:
            webbrowser.open(f"https://in.search.yahoo.com/search;_ylt=AwrxiDbKPVhhYhQA_RG6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANNdTQ1U0ZyeFRKRzhHdWU3cmFrU1pBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNQRxdWVyeQNoZWxsbwR0X3N0bXADMTYzMzE3Mjk1MQ--?p={cm}&fr=sfp&iscqry=&fr2=sb-top-search")

        else:
            url = f"https://www.google.com/search?q={cm}"
            webbrowser.open(f"{url}")
   
    def shay():
        Shayari = (

            "अर्ज किया है... वो तुम्हें Dp दिखाकर गुमराह करेगी, मगर तुम आधार कार्ड पर अड़े रहना।",

            "काश प्यार का इन्शुरन्स हो जाता, प्यार करने से पहले प्रीमियम भरवाया जाता. प्यार में वफ़ा मिली तो ठीक वर्ना, बेवफाओं पे जो खर्चा होता उसका क्लेम तो मिल जाता।",

            "मेरी प्रेम कहानी का क्या अजीब एंडिंग था, मेरी प्रेम कहानी का क्या अजीब एंडिंग था, मैंने प्रोपोज़ किआ SMS से, कमबख्त वह उसकी शादी तक पेंडिंग था।",

            "ताजमहल किसी के लिए एक अजूबा है, तो किसी के लिए प्यार का एहसास है, हमारे तुम्हारे लिए तो बकवास है, क्यूँ की की रोज़ बदलती हमारी मुम्ताज़ है।",

            "अजब सी हालत है तेरे जाने के बाद, मुझे भूख लगती नहीं खाना खाने के बाद, मेरे पास दो ही समोसे थे जो मैंने खा लिए, एक तेरे आने से पहले, एक तेरे जाने के बाद।",

            "ए गुलाब अपनी खुशबू को मेरे दोस्तों पर न्योछावर कर दे, यह सर्दी के मौसम में अक्सर नहाया नहीं करते।",

            "देखा है तुम्हारे आगे, शर्मा के फूलों को मुरझाते, ए जहाँ को घायल करने वाले तुम डिओडोरेंट क्यों नहीं लगाते।",

            "आज कुछ शर्माए से लगते हो, सर्दी के कारण कपकपए से लगते हो, चेहरा आपका खिलखिलाये सा लगता है, हफ्ते के बाद नहाए से लगते हो।",

            "खुद का बच्चा रोये तो दिल में दर्द होता है, किसी और का रोये तो सर में दर्द होता है, खुद की बीवी रोये तो भी सर में दर्द होता है, किसी और की रोये तो दिल में दर्द होता है।",

            "जब हम उनके घर गए... कहने दिल से दिल लगा लो, उनकी माँ ने खोला दरवाजा, हम घवरा के बोले.. आंटी बच्चो को पोलियो ड्राप पिलवा लो।",

            "इश्क के चर्चे बहुत हैं दोस्तों, हुस्न के पर्चे बहुत है यारों, इश्क करने से पहले जान लेना, इसमें खर्चे बहुत है दोस्तो।",

            "कुछ बोलूं तो इतराते बहुत हो, जानेमन तुम मुस्कुराते बहुत हो, मन करता है तुम्हे दावत पर बुलाऊँ, लेकिन जानेमन तुम खाते बहुत हो।",

            "जब कोई ज़िन्दगी में बहुत ख़ास बन जाए, उसके बारे में सोचना ही उसका एहसास बन जाए, तो मांग लेना खुदा से उसे जिंदगी भर के लिए, इस से पहले की उसकी माँ किसी और की सास बन जाए।",

            "जब तिरछी नजरों से उन्होंने हमको देखा, तो हम मदहोश हो गए जब पता लगा उनकी नज़रें ही तिरछी हैं तो हम बेहोश हो गए।",

            "नजर न लग जाये आँखों में काजल लगा लो, हम कहते हैं आँखों में काजल ही नहीं, हो सके तो... गले में नीबू मिर्ची चप्पल भी लटका लो,",

            "मीठी मीठी यादों को पलकों पे सजा लेना, साथ गुज़रे लम्हों को दिल में बसा लेना, मैं तो बरसों का प्यासा हूँ, फराज़ बिजली आ जाये तो याद से मोटर चला देना।",

            "मेरी ख़ुशी के लम्हे इस कदर मुख़्तसर हैं फ़राज़, अभी मुजरा शुरू ही हुआ था के छापा पड़ गया।",

            "मासूम सी मुहब्बत का फ़राज़ बस इतना सा फ़साना है.. अम्मी घर से निकलने नहीं देती और मुझी डेट पर जाना है।",
            
            "मोहब्बत करते हैं लोग बड़े शोर के साथ, हमने भी बड़े जोर के साथ, लेकिन अब करेंगे थोड़ा गौर के साथ, क्योंकि कल उसे देखा है किसी और के साथ।",
            
            "दोस्तो हम उन्हें मुड़ मुड़कर देखते रहे, और वो हमें मुड़-मुड़ कर देखते रहे, वो हमें हम उन्हें, वो हमें हम उन्हें, क्योंकि परीक्षा में न उन्हें कुछ आता था न हमे।",

            "जब दरवाजा खोलने गये तो चेहरे पर हसी थी, दरवाजा खोला तो आँखों में आँसू दिल में बेबसी थी, ज्यादा मत सोच पगले, मेरी ऊँगली दरवाजे में फंसी थी,",

            "फिजाओं के बदलने का इंतज़ार मत कर, आँधियों के रुकने का इंतज़ार मत कर, पकड़ किसी को और फरार हो जा, पापा की पसंद का इंतज़ार मत कर",

            "आपकी याद में एक शायर अर्ज़ किया है, आज है मंगल कल था पीर-वह-वह, कभी तो कुछ भेजा कर फकीर",

            "इश्क में ख्याल बहुत है इश्क के चर्चे बहुत है, सोचते है हम भी करले इश्क पर सुना है इश्क में खर्चे बहुत है",

            "और भी चीजें बहुत सी लुट चुकी है दिल के साथ, ये बताया दोस्तों ने इश्क फरमाने के बाद, इसलिए कमरे की एक एक चीज़ चेक करता हूँ, एक तेरे आने से पहले एक तेरे जाने के बाद")
        
        shay = random.choice(Shayari)
        tts = gTTS(text=shay, lang="hi", slow=False)
        filename = "Resources/Sound/my.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)

    def loc():
        say("Wait sir, let me check")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            url = 'http://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            #print(geo_data)
            city = geo_data['city']
            # state = geo_data['state']
            country = geo_data['country']
            say(f"Sir i am not sure, but i think we are in {city} city of {country} country")
        except Exception as e:
            say("Sorry sir, Due to network issue i am not able to find where we are.")
            pass

    def but(query):

        if "copy" in query:
            say("Copied")
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')

        elif "cut" in query or "move" in query:
            say("Moved")
            pyautogui.keyDown('ctrl')
            pyautogui.press('x')
            pyautogui.keyUp('ctrl')

        elif "save" in query:
            say("Okay saved")
            pyautogui.keyDown('ctrl')
            pyautogui.press('s')
            pyautogui.keyUp('ctrl')

        elif "paste" in query:
            say("Paste")
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')

    def insta():
        say("Sir please enter the user name correctly.")
        name = input("Enter username here:")
        webbrowser.open(f"www.instagram.com/{name}")
        say(f"Sir here is the profile of the user {name}")
        mod = instaloader.Instaloader() #pip install instadownloader
        mod.download_profile(name, profile_pic_only=True)
        say("I am done sir, profile picture is saved in our main folder. now i am ready")

    def news():
        say("Tell me the language for news Hindi or English")
        while True:
            new = takecom()
            if "none" in new:
                say("Please sir tell me the language for news Hindi or English")
            elif "hindi" in new:
                say("Ok here's the latest news.")
                say("Please wait sir, fetching the latest news")
                main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6ec6c6654b4148388ee77f582a34ce6e'
                main_page = requests.get(main_url).json()
                #print(main_page)
                articles = main_page["articles"]
                #print(articles)
                head = []
                day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
                for ar in articles:
                    head.append(ar["title"])
                for i in range (len(day)):
                    # say(f"Today's {day[i]} news is: {head[i]}")
                    line = f"today's {day[i]} news is: {head[i]}"
                    print(line)
                    All.Translate(line)
                say("This was some of today's latest news.")
                break
            elif "english" in new:
                say("Ok here's the latest news.")
                say("Please wait sir, fetching the latest news")
                main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6ec6c6654b4148388ee77f582a34ce6e'
                main_page = requests.get(main_url).json()
                #print(main_page)
                articles = main_page["articles"]
                #print(articles)
                head = []
                day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
                for ar in articles:
                    head.append(ar["title"])
                for i in range (len(day)):
                    line = f"today's {day[i]} news is: {head[i]}"
                    say(line)
                break
            else:
                say("Invalid language in your system")
                say("Please choose valid option")

    def Translate(line):
        translate = Translator()
        result = translate.translate(line, dest='hi')
        Text = result.text
        tts = gTTS(text=Text, lang="hi", slow=False)
        filename = "my.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)

    def downloader():
        root = Tk()
        root.geometry('500x300')
        root.resizable(0,0)
        root.title("Youtube Video Downloader")

        Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').place()
        link = StringVar()
        Label(root,text = 'Paste Yt Video URL Here',font = 'arial 15 bold').place(x=160,y=60)
        Entry(root, width=70, textvariable = link).place(x=32,y=90)

        def VideoDownloader():
            url = YouTube(str(link.get()))
            video = url.streams.first()
            video.download()
            Label(root, text = "Downloaded", font = 'arial 15').place(x=180,y=210)

        Button(root, text = "Download", font = 'arial 15 bold', bg = 'pale violet red', padx=2, command = VideoDownloader).place(x=180,y=150)
        
        root.mainloop()
        say("Video Downloaded")

    def Astro(start_date,end_date):
        Nasa_Api_Key = "LtVaRrrJGeg7q0aoddoTsbkwavqJ04NGmu2QEM9z"
        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Nasa_Api_Key}"
        r = requests.get(url)
        Data = r.json()
        Total_Astro = Data['element_count']
        neo = Data['near_earth_objects']
        say(f"Total Astroid Between {start_date} to {end_date} Is : {Total_Astro}")
        say("Extact Data For Those Astroids Are Listed Below .")
        for body in neo[start_date]:
            id = body['id']
            name = body['name']
            absolute = body['absolute_magnitude_h']
            take = id, name, absolute
            say(take)

    def alarm(Timing):
        altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))

        altime = altime[11:-3]

        Horeal = altime[:2]
        Horeal = int(Horeal)
        Mireal = altime[3:5]
        Mireal = int(Mireal)
        print(f"Done, alarm is set for {Timing}")

        while True:
            if Horeal==datetime.datetime.now().hour:
                if Mireal==datetime.datetime.now().minute:
                    print("Alarm is runing")
                    playsound("Resources/Sound/twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3")

                elif Mireal<datetime.datetime.now().minute:
                    break

    def typing(query):

        if "cmd" in query:
            say("Opening cmd")
            os.system("start cmd")
            say("Sir, what should i type")
            while True:
                gm = takecom()
                if "none" in gm:
                    say("Please sir tell me what should i type")

                elif "stop" in gm or "enter" in gm:
                    pyautogui.press("Enter")
                    say(f"Okay! sir i am type {gm}")
                    break

                elif "exit" in gm:
                    say("Exiting...")
                    pyautogui.keyDown('alt')
                    pyautogui.press('f4')
                    pyautogui.keyUp('alt')
                    
                else:
                    gm = gm.replace("exit", "")
                    gm = gm.replace("stop", "")
                    gm = gm.replace("none", "")
                    pyautogui.typewrite(f"{gm}")

        elif "notepad" in query:
            vpath = "C:\\Windows\\system32\\notepad.exe"
            say("Opening notepad")
            os.startfile(vpath)
            say("Tell me what to write")
            while True:
                ty = takecom()
                if "exit" in ty:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('s')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('1')
                    pyautogui.press("Enter")
                    say("Saved")
                    say("Exiting...")
                    pyautogui.keyDown('alt')
                    pyautogui.press('f4')
                    pyautogui.keyUp('alt')
                    break

                elif "stop" in ty:
                    say("Typing Stoped")
                    break
                
                elif "none" in ty:
                    say("Please sir tell me what should i type")

                elif "save" in ty:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('s')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('1')
                    pyautogui.press("Enter")
                    say("Saved your data")
                    break
                
                else:
                    pyautogui.typewrite(f'{ty} ')

    def home(query, board):
        if "light on" in query:
            say("Light On...")
            board.digital[7].write(0)

        elif "light off" in query:
            say("Light Off...")
            board.digital[7].write(1)

        elif "sayer on" in query:
            board.digital[6].write(0)
            say("sayer On...")

        elif "sayer off" in query or "sayer of" in query:
            say("sayer Off...")
            board.digital[6].write(1)

    def bat():
        battery = psutil.sensors_battery()  
        percentage = battery.percent
        say(f"Sir our system have {percentage} percent charging")
        if percentage>=75:
            say("We have enough power to continue our work")
        elif percentage>=40 and percentage<=75:
            say("We should connect our system to charging point to charge our battery")
        elif percentage<=15 and percentage>=40:
            say("We don't have enough power to work, please connect to charging")
        elif percentage<=15:
            say("We have very low power, please connect to charging the system will shutdown very soon")

    def ChatterBot(Text):
        Hello = ('hello','hey','hii','hi')
        reply_Hello = ('Hello Sir , I Am Alexa.',
                    "Hey , What's Up ?",
                    "Hey How Are You ?",
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
        Text = str(Text)
        for word in Text.split():
            
            if word in Hello:
                reply = random.choice(reply_Hello)
                say(reply)
                return reply

            elif word in Bye:
                reply = random.choice(reply_bye)
                say(reply)
                return reply

            elif word in How_Are_You:
                reply_ = random.choice(reply_how)
                say(reply_)
                return reply_

            elif word in Functions:
                reply___ = random.choice(reply_Functions)
                say(reply___)
                return reply___

            else:
                ret = random.choice(sorry_reply)
                say(ret)
                return ret

    def onoff(ans):
        if "on" in ans:
            if __name__ == "__main__":
                asyncio.run(All.BluetoothOn("on"))

        else:
            if __name__ == "__main__":
                asyncio.run(All.BluetoothOn("off"))

    def lit():
        while True:
            yu = takecom()
            
            if "exit" in yu or "close" in yu:
                say("Exiting...")
                break

            elif "none" in yu:
                say("Please sir tell me anything")

            else:
                yu = yu.replace("exit","")
                yu = yu.replace("none","")
                max_results = 1
                how_to = search_wikihow(yu, max_results)
                assert len(how_to) == 1
                line = how_to[0].summary
                say("Choose Language:")
                say("1 : Hindi")
                say("2 : English")
                lang = takecom()
                say("Please wait fetching a details")
                if "hindi" in lang:
                    print(line)
                    translate = Translator()
                    result = translate.translate(line, dest='hi')
                    Text = result.text
                    tts = gTTS(text=Text, lang="hi", slow=False)
                    filename = "my.mp3"
                    tts.save(filename)
                    playsound(filename)
                    os.remove(filename)
                    break
                elif "exit" in lang:
                    say("Exiting...")
                    break
                
                elif "english" in lang:
                    say(line)
                    
                else:
                    say("Please sir choose language:")
                    say("1 : Hindi")
                    say("2 : English")

    def pdf():
        book = open('py3.pdf')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        say(f"Total number of pages in this book {pages} ")
        say("sir, please enter the page number i have to read")
        pg = int(input("Please enter the page number: "))
        page = pdfReader.getPage(pg)
        text = page.extract()
        say(text)

    def hide():
        say("Sir please tell me you want to hide this folder or make it visible for everyone")
        while True:
            condition = takecom()
            if "hide" in condition or "invisible" in condition:
                os.system("attrib +h /s /d")
                say("Sir, all the files in this folder are now hidden")
                break
            elif "visible" in condition or "unhide" in condition:
                os.system("attrib -h /s /d")
                say("Sir, all the files in this folder are now visible to everyone. i wish yu are taking")
                break

            elif "leave it" in condition or "leave for now" in condition or "exit" in condition or "close" in condition:
                say("Okay sir")
                break
            
            elif "none" in condition:
                say("Please sir tell me how it work")
