from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
from Resources.Scripts.Sound import speak

def downloader():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Youtube Video Downloader")

    Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').place()
    link = StringVar()
    Label(root,text = 'Paste Yt Video URL Here',font = 'arial 15 bold').place(x=160,y=60)
    Entry(root, width=70, textvariable = link).place(x=32,y=90)

    def VideoDownloader():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(root, text = "Downloaded", font = 'arial 15').place(x=180,y=210)

    Button(root, text = "Download", font = 'arial 15 bold', bg = 'pale violet red', padx=2, command = VideoDownloader).place(x=180,y=150)
    
    root.mainloop()
    speak("Video Downloaded")

downloader()