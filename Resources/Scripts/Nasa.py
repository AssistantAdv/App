import requests
from Resources.Scripts.Trans import Translate
import os
from Resources.Scripts.Sound import speak
from Resources.Scripts.Sound import takecom
from PIL import Image

Api_Key = "LtVaRrrJGeg7q0aoddoTsbkwavqJ04NGmu2QEM9z"

def Nasanews(Date):
    speak("Extracting data from Nasa.")
    Url = f"https://api.nasa.gov/planetary/apod?api_key={Api_Key}"
    Params = {'date':str(Date)}
    r = requests.get(Url,params = Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    path_1 = "C:\\Users\\HP\\OneDrive\\Desktop\\AI\\Jarvis\\" + str(FileName)
    path_2 = "C:\\Users\\HP\\OneDrive\\Desktop\\AI\\Jarvis\\Jarvis 2.0.0\\Database\\Nasa_photos\\" + str(FileName)
    os.rename(path_1, path_2)
    img = Image.open(path_2)
    img.show()
    line = f"Title : {Title}"
    line_2 = f"According to Nasa {Info}"
    speak("Tell me news in Hindi or English")
    la = takecom()
    if "hindi" in la:
        print(line)
        print(line_2)
        Translate(line)
        Translate(line_2)
    else:
        speak(f"Title : {Title}")
        speak(f"According to Nasa {Info}")
    os.remove(path_2)

def Images(pt):
    name = 'curiosity'
    date = '2020-12-3'
    Api_ = str(Api_Key)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_}"
    r = requests.get(url)
    Data = r.json()
    Photos = Data['photos'][:pt]
    try:
        for index , photo in enumerate(Photos):
            camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = camera['name']
            full_camera_name = camera['full_name']
            date_of_photo = photo['earth_date']
            img_url = photo['img_src']
            p = requests.get(img_url)
            img = f'{index}.jpg'
            with open(img,'wb') as file:
                file.write(p.content)
            path_1 = "C:\\Users\\HP\\OneDrive\\Desktop\\AI\\Jarvis\\" + str(img)
            path_2 = "C:\\Users\\HP\\OneDrive\\Desktop\\AI\\Jarvis\\Jarvis 2.0.0\\Database\\Nasa photos\\" + str(img)
            os.rename(path_1,path_2)
            os.startfile(path_2)
            line = f"This image was captured with : {full_camera_name}"
            Translate(line)
            # speak(f"This image was captured with : {full_camera_name}")
            # speak(f"This image was captured on : {date_of_photo}")
            line_2 = f"This image was captured on : {date_of_photo}"
            Translate(line_2)
            os.remove(path_2)

    except:
        speak("There is an error")

def Astro(start_date,end_date):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
    r = requests.get(url)
    Data = r.json()
    Total_Astro = Data['element_count']
    neo = Data['near_earth_objects']
    speak(f"Total Astroid Between {start_date} to {end_date} Is : {Total_Astro}")
    speak("Extact Data For Those Astroids Are Listed Below .")
    for body in neo[start_date]:
        id = body['id']
        name = body['name']
        absolute = body['absolute_magnitude_h']
        take = id, name, absolute
        speak(take)





