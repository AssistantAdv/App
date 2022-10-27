import requests
from Resources.Scripts.Sound import speak

def loc():
    speak("Wait sir, let me check")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        url = 'http://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        #print(geo_data)
        city = geo_data['city']
        # state = geo_data['state']
        country = geo_data['country']
        speak(f"Sir i am not sure, but i think we are in {city} city of {country} country")
    except Exception as e:
        speak("Sorry sir, Due to network issue i am not able to find where we are.")
        pass

