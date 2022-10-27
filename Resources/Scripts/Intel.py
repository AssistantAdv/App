from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
from pywikihow import search_wikihow
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

def lit():
    while True:
        yu = takecom()
        
        if "exit" in yu or "close" in yu:
            speak("Exiting...")
            break

        elif "none" in yu:
            speak("Please sir tell me anything")

        else:
            yu = yu.replace("exit","")
            yu = yu.replace("none","")
            max_results = 1
            how_to = search_wikihow(yu, max_results)
            assert len(how_to) == 1
            line = how_to[0].summary
            speak("Choose Language:")
            speak("1 : Hindi")
            speak("2 : English")
            lang = takecom()
            speak("Please wait fetching a details")
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
                speak("Exiting...")
                break
            
            elif "english" in lang:
                speak(line)
                
            else:
                speak("Please sir choose language:")
                speak("1 : Hindi")
                speak("2 : English")
