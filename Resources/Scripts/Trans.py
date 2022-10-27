from googletrans import Translator
from playsound import playsound
from gtts import gTTS
import os

def Translate(line):
    translate = Translator()
    result = translate.translate(line, src='en' ,dest='hi')
    print(result)
    Text = result.text
    tts = gTTS(text=Text, lang="hi", slow=False)
    filename = "my.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
