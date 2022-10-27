import pyautogui
import time
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
import os

def msg():
    speak("Choose")
    speak("1 : Text message")
    speak("2 : Whatsapp message")
    while True:
        pi = takecom()
        
        if "text" in pi:
            speak("Sir what should i send a message")
            while True:
                msz = takecom()
                if "none" in msz:
                    speak("Please tell me what should i send message")
                elif "exit" in msz:
                    speak("Exiting...")
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
            break
        
        elif "whatsapp" in pi:
            apath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("Opening Whatsapp")
            os.startfile(apath)
            time.sleep(10)
            speak("Tell me name of the person send message")
            while True:
                tk = takecom()

                if "prashik" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('+918459897248')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "saurabh" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('+919307956971')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "sanjana" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('+918010660771')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "abhishek" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('+917499352296')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "pooja" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('+919730601589')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "alpha computer" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('alpha computer')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("This group is only admin send message")

                elif "c programe" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('c programe')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "free fire" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('༆₲øĐ〠ຮᴛαʀ࿐ Family')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "family" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('best family group')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "friends" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('cricket team')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "whitehat" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('whitehat')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "nagpur" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('रॉयल ग्रुप नागपुर')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "school" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('👨‍❤‍💋‍👨👩‍❤‍💋‍👩School ki yaade😍😎')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "nirmal" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('Nirmal shahu')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "shubham" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('shubham')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "ashish" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('आशिश')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "click" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('click internet')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "dhruv" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('dhruv')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "sandip" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('sandip university')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "kunal" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('kunal nimje')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "prashik 2" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('पृशिक')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            pyautogui.keyDown('alt')
                            pyautogui.press('f4')
                            pyautogui.keyUp('alt')
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "sanjana 2" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('+919699264118')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "mohata" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('mohota')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "bhumesh" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('bhumesh')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "c programe" in tk:
                    pyautogui.keyDown('ctrl')
                    pyautogui.press('f')
                    pyautogui.keyUp('ctrl')
                    time.sleep(1)
                    pyautogui.typewrite('c programe')
                    time.sleep(1)
                    pyautogui.press('down')
                    time.sleep(1)
                    pyautogui.press('Enter')
                    speak("Tell me message")
                    while True:
                        message = takecom()
                        if "send" in message:
                            speak("Sending...")
                            pyautogui.press('Enter')
                            break
                        elif "none" in message:
                            speak("Please sir tell me message")
                        elif "exit" in message:
                            speak("Exiting...")
                            break
                        else:
                            message = message.replace("send","")
                            message = message.replace("none", "")
                            message = message.replace("exit", "")
                            pyautogui.typewrite(f'{message} ')
                    break

                elif "exit" in tk:
                    speak("Exiting...")
                    break

                elif "no send" in tk:
                    speak("Okay not sending message")
                    break

                elif "none" in tk:
                    speak("Please sir tell me name of the person send message")

                else:
                    speak("Invalid person")
                    speak("Please valid person choose in your whatsapp")
            break

        elif "none" in pi:
            speak("Please sir choose")
            speak("1 : Text message")
            speak("2 : Whatsapp message")
            pi = takecom()

        elif "exit" in pi:
            speak("Exiting...")
            break

        else:
            speak("Invalid choice")
            speak("Please sir choose valid choice")
            pi = takecom()