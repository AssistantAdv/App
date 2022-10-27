import os
import sqlite3

audacity = ["audacity", "Audacity.exe"]
azure = ["azure data studio", "azuredatastudio.exe"]
bluestack = ["bluestack", "HD-Player.exe"]
database = ["database", "DB Browser for SQLite.exe"]
internetexplorer = ["internet explorer", "iexplore.exe"]
pycharm = ["pycharm", "pycharm64.exe"]
obs = ["obs studio", "obs64.exe"]
opera = ["opera browser", "opera.exe"]
team = ["team viewer", "TeamViewer.exe"]
vlc = ["vlc", "vlc.exe"]
media = ["media player", "wmplayer.exe"]
wordpad = ["wordpad", "wordpad.exe"]
Zip = ["zip", "WinRAR.exe"]
notepad = ["notepad", "notepad.exe"]
setting = ["setting", "control.exe"]
cmd = ["cmd", "cmd.exe"]
paint = ["ms paint", "mspaint.exe"]
mip = ["mip", "mip.exe"]
car = ["character map", "charmap.exe"]
ass = ["assistant", "quickassist.exe"]
sniping = ["snipping tool", "SnippingTool.exe"]
remote = ["remote desktop", "mstsc.exe"]
reco = ["step recorder", "psr.exe"]
fax = ["fax and scan", "WFS.exe"]
pagemaker = ["pagemaker", "Pm70.exe"]
reader = ["reader", "AcroRd32.exe"]
dev = ["dev c++", "devcpp.exe"]
chrome = ["chrome browser", "chrome.exe"]
mini = ["mini player", "mpc-hc.exe"]
edge = ["edge", "msedge.exe"]
sql = ["sql server", "DTASHELL.EXE"]
visual = ["visual studio tools", "vsta.exe"]
firefox = ["firefox browser", "firefox.exe"]
nsis = ["nsis", "NSIS.exe"]
qtdesigner = ["qt designer", "designer.exe"]
typing = ["typing master", "tmaster.exe"]
vmware = ["vmware", "vmware.exe"]
wo = ["wo mic", "WOMicClient.exe"]
whatsapp = ["whatsapp", "WhatsApp.exe"]
vscode = ["vs code", "Code.exe"]
telegram = ["telegram", "Telegram.exe"]
typing1 = ["typing master 11", "TypingMaster.exe"]

all = [audacity, azure, bluestack, database, internetexplorer, pycharm, obs, opera, team, vlc, media, wordpad, Zip, pagemaker, reader, dev, chrome, mini, edge, sql, visual, firefox, nsis, qtdesigner, typing, vmware, wo, whatsapp, vscode, telegram, typing1]

def application():
    connection = sqlite3.connect('Resources/Database/AiDatabase.db')
    cursor = connection.cursor()
    try:
        cursor.execute('CREATE TABLE Application(Name TEXT, Path TEXT)')
        connection.commit()
    except:
        pass
    try:
        cursor.execute('CREATE TABLE App_not_found(Name TEXT, extension TEXT)')
        connection.commit()
    except:
        pass
    for a in all:
        cursor.execute(f"SELECT Name FROM App_not_found WHERE Name='{a[0]}'")
        nf = cursor.fetchone()
        if nf == None:
            name = a[0]
            cursor.execute(f"SELECT Name FROM Application WHERE Name='{name}'")
            us = cursor.fetchone()
            if us == None:
                search = a[1]
                print(f"{a[0]} searching...")
                listen = os.walk("C:\\")
                for root_path, directories, files, in listen:
                    if search in files:
                        file_found = True
                        path_app = os.path.join(root_path, search)
                        ap = [a[0], path_app]
                        cursor.execute("INSERT INTO Application VALUES(?, ?)", ap)
                        connection.commit()
                        print(f"{a[0]} added")

                        break
                else:
                    apnf = [a[0], a[1]]
                    cursor.execute("INSERT INTO App_not_found VALUES(?, ?)", apnf)
                    connection.commit()
                    print(f"{a[0]} not found")
                
            else:
                print(f"{a[0]} already added")
        
        else:
            continue
    print("Deleting table")
    cursor.execute("DELETE FROM App_not_found")
    connection.commit()
                
def applicationcl(appl):
    for a in all:
        if appl == a[0]:
            os.system(f"taskkill /f /im {a[1]}")
    else:
        os.system("taskkill /f /im chrome.exe")

def websites():
    connection = sqlite3.connect('Resources/Database/AiDatabase.db')
    cursor = connection.cursor()
    youtube = ["youtube","www.youtube.com"]
    facebook = ["facebook", "www.facebook.com"]
    amazon = ["amazon", "www.amazon.com"]
    google = ["google", "www.google.com"]
    flipkart = ["flipkart", "www.flipkart.com"]
    snapdeal = ["snapdeal", "www.snapdeal.com"]
    ebay = ["ebay", "www.ebay.com"]
    gmail = ["gmail", "www.gmail.com"]
    stackoverflow = ["stackoverflow", "www.stackoverflow.com"]
    github = ["github", "www.github.com"]
    instagram = ["instagram", "www.instagram.com"]
    yahoo = ["yahoo", "www.yahoo.com"]

    web_all = [youtube, facebook, amazon, google, flipkart, snapdeal, ebay, gmail, stackoverflow, github, instagram, yahoo]

    try:
        cursor.execute('CREATE TABLE Application(Name TEXT, Path TEXT)')
        connection.commit()
    except:
        pass
    for web in web_all:
        cursor.execute(f"SELECT Name FROM Application WHERE Name='{web[0]}'")
        name = cursor.fetchone()
        if name == None:
            cursor.execute(f"SELECT Path FROM Application WHERE Name='{web[1]}'")
            path = cursor.fetchone()
            if path == None:
                ap = [web[0], web[1]]
                cursor.execute("INSERT INTO Application VALUES(?, ?)", ap)
                connection.commit()
            else:                
                pass
        else:
            pass

def system_app(query):
    
    if "calculator" in query:
        os.system("start calc")
    elif "paint" in query:
        os.system("start mspaint")
    elif "notepad" in query:
        os.system("start notepad")
    elif "remote desktop" in query:
        os.system("start mstsc")
    elif "onscreen keyboard" in query:
        os.system("start osk")
    elif "wordpad" in query:
        os.system("start write")
    elif "this pc" in query:
        os.system("start explorer")
    elif "character map" in query:
        os.system("start charmap")
    elif "control panel" in query:
        os.system("start control")
    elif "ip address" in query:
        os.system("start ipconfig")
    elif "system information" in query:
        os.system("start msinfo32")
    elif "task manager" in query:
        os.system("start taskmgr")
    else:
        os.open('dvdfhbvfd')

