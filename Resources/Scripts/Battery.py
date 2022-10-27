import psutil
from Resources.Scripts.Sound import speak

def bat():
    battery = psutil.sensors_battery()  
    percentage = battery.percent
    speak(f"Sir our system have {percentage} percent charging")
    if percentage>=75:
        speak("We have enough power to continue our work")
    elif percentage>=40 and percentage<=75:
        speak("We should connect our system to charging point to charge our battery")
    elif percentage<=15 and percentage>=40:
        speak("We don't have enough power to work, please connect to charging")
    elif percentage<=15:
        speak("We have very low power, please connect to charging the system will shutdown very soon")