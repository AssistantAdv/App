import requests
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
from Resources.Scripts.Trans import Translate

def news():
    speak("Tell me the language for news Hindi or English")
    while True:
        new = takecom()
        if "none" in new:
            speak("Please sir tell me the language for news Hindi or English")
        elif "hindi" in new:
            speak("Ok here's the latest news.")
            speak("Please wait sir, fetching the latest news")
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
                # speak(f"Today's {day[i]} news is: {head[i]}")
                line = f"today's {day[i]} news is: {head[i]}"
                print(line)
                Translate(line)
            speak("This was some of today's latest news.")
            break
        elif "english" in new:
            speak("Ok here's the latest news.")
            speak("Please wait sir, fetching the latest news")
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
                speak(line)
                print(line)
                Translate(line)
            speak("This was some of today's latest news.")
            break
        else:
            speak("Invalid language in your system")
            speak("Please choose valid option")
    # speak("This was some of today's latest news.")
    # speak("Please wait sir, fetching the latest news")
    # if "hindi" in new:
    #     main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6ec6c6654b4148388ee77f582a34ce6e'
    #     main_page = requests.get(main_url).json()
    #     #print(main_page)
    #     articles = main_page["articles"]
    #     #print(articles)
    #     head = []
    #     day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    #     for ar in articles:
    #         head.append(ar["title"])
    #     for i in range (len(day)):
    #         # speak(f"Today's {day[i]} news is: {head[i]}")
    #         line = f"today's {day[i]} news is: {head[i]}"
    #         print(line)
    #         Translate(line)

    # else:
    #     main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=6ec6c6654b4148388ee77f582a34ce6e'
    #     main_page = requests.get(main_url).json()
    #     #print(main_page)
    #     articles = main_page["articles"]
    #     #print(articles)
    #     head = []
    #     day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    #     for ar in articles:
    #         head.append(ar["title"])
    #     for i in range (len(day)):
    #         line = f"today's {day[i]} news is: {head[i]}"
    #         speak(line)

 