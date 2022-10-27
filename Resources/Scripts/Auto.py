import os
import pyautogui
import time
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom

def typeing(query):

    if "cmd" in query:
        speak("Opening cmd")
        os.system("start cmd")
        speak("Sir, what should i type")
        while True:
            gm = takecom()
            if "none" in gm:
                speak("Please sir tell me what should i type")

            elif "stop" in gm or "enter" in gm:
                pyautogui.press("Enter")
                speak(f"Okay! sir i am type {gm}")
                break

            elif "exit" in gm:
                speak("Exiting...")
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
        speak("Opening notepad")
        os.startfile(vpath)
        speak("Tell me what to write")
        while True:
            ty = takecom()
            if "exit" in ty:
                pyautogui.keyDown('ctrl')
                pyautogui.press('s')
                pyautogui.keyUp('ctrl')
                time.sleep(1)
                pyautogui.typewrite('1')
                pyautogui.press("Enter")
                speak("Saved")
                speak("Exiting...")
                pyautogui.keyDown('alt')
                pyautogui.press('f4')
                pyautogui.keyUp('alt')
                break

            elif "stop" in ty:
                speak("Typing Stoped")
                break
            
            elif "none" in ty:
                speak("Please sir tell me what should i type")

            elif "save" in ty:
                pyautogui.keyDown('ctrl')
                pyautogui.press('s')
                pyautogui.keyUp('ctrl')
                time.sleep(1)
                pyautogui.typewrite('1')
                pyautogui.press("Enter")
                speak("Saved your data")
                break
            
            else:
                pyautogui.typewrite(f'{ty} ')

def home(query, board):

    if "light on" in query:
        speak("Light On...")
        board.digital[7].write(0)

    elif "light off" in query:
        speak("Light Off...")
        board.digital[7].write(1)

    elif "speaker on" in query:
        board.digital[6].write(0)
        speak("Speaker On...")

    elif "speaker off" in query or "speaker of" in query:
        speak("Speaker Off...")
        board.digital[6].write(1)



                