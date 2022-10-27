from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
import webbrowser
import wikipedia

def search(query):
    
    if "youtube" in query:
        speak("Sir, what should i search on youtube")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break

            elif "none" in cm:
                speak("Please sir, tell me what should i search on youtube")
            
            else :
                webbrowser.open(f"http://www.youtube.com/results?search_query={cm}")
                speak(f"Searching youtube on {cm}")
                break
    
    elif "google" in query:
        speak("What should i search on google")
        while True:
            search = takecom()
            if "none" in search:
                speak("Please tell me what should i search")

            elif "exit" in search:
                speak("Exiting...")
                break

            else:
                search = search.replace("none", "")
                search = search.replace("exit", "")
                url = f"https://www.google.com/search?q={search}"
                webbrowser.open(f"{url}")
                break

    elif "facebook" in query:
        speak("Sir, what should i search on facebook")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break
        
            elif "none" in cm:
                speak("Please sir, tell me what should i search on facebook")
                
            else:
                webbrowser.open(f"https://www.facebook.com/search/top?q={cm}")
                speak(f"Searching facebook on {cm}")
                break
            
    elif "amazon" in query:
        speak("Sir, what should i search on amazon")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break

            elif "none" in cm:
                speak("Please sir, tell me what should i search on amazon")
                
            else:
                webbrowser.open(f"https://www.amazon.com/s?k={cm}&ref=nb_sb_noss_2")
                speak(f"Searching amazon on {cm}")
                break

    elif "flipkart" in query:
        speak("Sir, what should i search on flipkart")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break

            elif "none" in cm:
                speak("Please sir, tell me what should i search on flipkart")
                
            else:
                webbrowser.open(f"https://www.flipkart.com/search?q={cm}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
                speak(f"Searching flipkart on {cm}")
                break

    elif "wikipedia" in query:
        speak("Sir, what should I search on wikipedia")
        while True:
            que = takecom()
            if "exit" in que or "searching" in que or "stop" in que:
                speak("Exiting...")
                break
            elif "none" in que:
                speak("Please sir, tell me what should I search on wikipedia")
            else:
                que = que.replace("exit", "")
                que = que.replace("none", "")
                results = wikipedia.summary(que, sentences=2)
                speak(f"{que} about {results}")
                speak("Many more information about")
                speak("Tell me yes or no")
                while True:
                    bm = takecom()
                    if "yes" in bm:
                        results = wikipedia.summary(que, sentences=10)
                        speak(f"okay! many more is {results}")
                        break
                    elif "no" in bm:
                        speak("okay! no more information")
                        break
                    elif "none" in bm:
                        speak("please sir tell me yes or no")

    elif "snapdeal" in query:
        speak("Sir, what should i search on snapdeal")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break

            elif "none" in cm:
                speak("Please sir, tell me what should i search on snapdeal")
                
            else:
                webbrowser.open(f"https://www.snapdeal.com/search?keyword={cm}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
                speak(f"Searching snapdeal on {cm}")
                break

    elif "ebay" in query:
        speak("Sir, what should i search on ebay")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break

            elif "none" in cm:
                speak("Please sir, tell me what should i search on ebay")
                
            else:
                webbrowser.open(f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={cm}&_sacat=0")
                speak(f"Searching ebay on {cm}")
                break

    elif "yahoo" in query:
        speak("Sir, what should i search on yahoo")
        while True:
            cm = takecom()
            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                speak("Okay sir, stop searching")
                break

            elif "none" in cm:
                speak("Please sir, tell me what should i search on yahoo")
                
            else:
                webbrowser.open(f"https://in.search.yahoo.com/search;_ylt=AwrxiDbKPVhhYhQA_RG6HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANNdTQ1U0ZyeFRKRzhHdWU3cmFrU1pBBG5fcnNsdAMwBG5fc3VnZwMxMARvcmlnaW4DaW4uc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNQRxdWVyeQNoZWxsbwR0X3N0bXADMTYzMzE3Mjk1MQ--?p={cm}&fr=sfp&iscqry=&fr2=sb-top-search")
                speak(f"Searching yahoo on {cm}")
                break

    elif "photos" in query:
        query = query.replace("photos", "")
        webbrowser.open(f"https://www.google.com/search?q={query}&source=Inms&tbm=isch&sa=X&ved=2ahUKEwjOh-G_ir3zAhV7xzgGHXB5AIAQ_AUoAXoECAEQAw")
        speak(f"There is {query} photos")

