import datetime
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
import PyPDF2
from Resources.Scripts.News import news

def wish():
    hour = int(datetime.datetime.now().hour)
    dt = datetime.datetime.now()
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak(dt.strftime("time %H:%M"))
    speak("Would like to hear today's latest news.")
    speak("Tell me yes or no")
    while True:
        new = takecom()
        if "yes" in new:
            news()
            speak("This was some of today's latest news.")
            break
        elif "no" in new:
            speak("Ok will not tell today's latest news.")
            break
        elif "none" in new:
            speak("Please sir tell me yes or no")
        else:
            speak("Sorry sir but I cant understand, try again")
    speak("Please tell me how can i help you sir.")

def pdf():
    book = open('py3.pdf', "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages} ")
    speak("sir, please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extract()
    speak(text)

