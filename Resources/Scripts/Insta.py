import webbrowser
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
import instaloader

def insta():
    speak("Sir please enter the user name correctly.")
    name = input("Enter username here:")
    webbrowser.open(f"www.instagram.com/{name}")
    speak(f"Sir here is the profile of the user {name}")
    speak("Sir would you like to download profile picture of this account.")
    speak("Tell me yes or no")
    while True:
        condition = takecom()
        if "yes" in condition:
            mod = instaloader.Instaloader() #pip install instadownloader
            mod.download_profile(name, profile_pic_only=True)
            speak("I am done sir, profile picture is saved in our main folder. now i am ready")
            break
        elif "no" in condition:
            speak("Okay sir, not download profile picture")
            break
        elif "none" in condition:
            speak("Please tell me sir yes or no")

