import datetime
from playsound import playsound

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
                playsound("C:\\Users\\HP\\OneDrive\\Desktop\\AI\\Jarvis\\Jarvis 2.0.0\\Database\\sound\\twirling-intime-lenovo-k8-note-alarm-tone-41440.mp3")

            elif Mireal<datetime.datetime.now().minute:
                break
