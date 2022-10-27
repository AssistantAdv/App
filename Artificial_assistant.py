import speech_recognition as sr, pywhatkit as kit, numpy as np, webbrowser, threading, pyautogui, wikipedia, datetime, pyttsx3, sqlite3, qrcode, psutil, autopy, time, random, math, cv2, sys, os
from PyQt5.QtWidgets import QFileDialog, QShortcut, QToolBar, QAction, QLineEdit, QMainWindow, QMessageBox, QDialog, QApplication, QWidget
from PyQt5.QtCore import QPropertyAnimation, QRect, QTimer, QTime, QDate, Qt, QUrl, QSize
from PyQt5.QtGui import QMovie, QImage, QPixmap, QKeySequence, QColor, QPainter
from Resources.Applications.login_or_register import Ui_login_or_register
from Resources.Scripts import Email_sender, HandTrackingModule as htm
from Resources.Applications.forget_password import Ui_forget_password
from Resources.Applications.forget_username import Ui_forget_username
from Resources.Applications.registration import Ui_registration
from Resources.Applications.showprofile import Ui_ShowProfile
from Resources.Applications.editprofile import Ui_EditProfile
from Resources.Applications.add_application import Ui_Add
from Resources.Applications.add_help import Ui_Add_help
from Resources.Applications.Main_login import Ui_login
from Resources.Applications.welcome import Ui_welcome
from Resources.Applications.Capture import Ui_Capture
from Resources.Applications.QrCode import Ui_QrCode
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Resources.Applications.Camera import Ui_Camera
from Resources.Applications.mouse import Ui_Mouse
from Resources.Applications.home import Ui_home
from PyQt5 import QtGui, QtCore, QtWidgets
from Resources.Scripts.All import All
from pyzbar.pyzbar import decode

use = [];tk = [];ls = [];sp = [];pt = [];ap1 = [];pt1 = [];ap2 = [];web = [];tm = [];msg = [];clth = [];pics = []

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def say(audio):
    sp.append(audio)
    ls.append("Speaking...")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate', 200)
    engine.say(audio)
    engine.runAndWait()

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        ls.append("Listening...")
        audio = r.listen(source, phrase_time_limit=4)
    try:
        print("Recoginizing...")
        ls.append("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        tk.append(query)
        print(f"user said : {query}")
    except:
        return "none"
    query = query.lower()
    return query

def close_thread():
    clth.append(1)

class ImageViewer(QWidget):
    pixmap = None
    _sizeHint = QSize()
    ratio = Qt.KeepAspectRatio
    transformation = Qt.SmoothTransformation
    def __init__(self, pixmap=None):
        super().__init__()
        self.setPixmap(pixmap)
    def setPixmap(self, pixmap):
        if self.pixmap != pixmap:
            self.pixmap = pixmap
            if isinstance(pixmap, QPixmap):
                self._sizeHint = pixmap.size()
            else:
                self._sizeHint = QSize()
            self.updateGeometry()
            self.updateScaled()
    def setAspectRatio(self, ratio):
        if self.ratio != ratio:
            self.ratio = ratio
            self.updateScaled()
    def setTransformation(self, transformation):
        if self.transformation != transformation:
            self.transformation = transformation
            self.updateScaled()
    def updateScaled(self):
        if self.pixmap:
            self.scaled = self.pixmap.scaled(self.size(), self.ratio, self.transformation)
        self.update()
    def sizeHint(self):
        return self._sizeHint
    def resizeEvent(self, event):
        self.updateScaled()
    def paintEvent(self, event):
        if not self.pixmap:
            return
        qp = QPainter(self)
        r = self.scaled.rect()
        r.moveCenter(self.rect().center())
        qp.drawPixmap(r, self.scaled)

class Image(qrcode.image.base.BaseImage):
    def __init__(self, border, width, box_size):
        self.border = border
        self.width = width
        self.box_size = box_size
        size = (width + border * 2) * box_size
        self._image = QImage(size, size, QImage.Format_RGB16)
        self._image.fill(Qt.white)
    def pixmap(self):
        return QPixmap.fromImage(self._image)
    def drawrect(self, row, col):
        painter = QPainter(self._image)
        painter.fillRect(
            (col + self.border) * self.box_size,
            (row + self.border) * self.box_size,
            self.box_size, self.box_size,
            QtCore.Qt.black)

class MainThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        self.TaskExecution()
    def TaskExecution(self):
        
        try:
            say("Hello sir")
            while True:
                query = takecom()
                if clth[0] == 1:
                    break
                elif "close profile" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(6)
                elif "edit" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(7)
                elif "my profile" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(1)
                elif "hide" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(9)
                elif "show" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(10)
                elif "home" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(2)
                elif "back" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(8)
                elif "feature" in query or "features" in query:
                    say("Yes sir")
                    tm.pop(0)
                    tm.append(3)
                elif "quit" in query or "exit" in query or "terminate" in query:
                    tm.pop(0)
                    tm.append(4)

                    say("Are you sure to terminating?")
                    check = takecom()
                    if "yes" in check:
                        say("Okay sir, terminating...")
                        exit()
                    else:
                        say("Okay sir, i am not terminating...")
                elif "logout" in query or "log out" in query:
                    tm.pop(0)
                    tm.append(5)
                    say("Are you sure to logout")
                    check = takecom()
                    if "yes" in check:
                        say("Logout now...")
                        pyautogui.press("left")
                        pyautogui.press("enter")
                        break
                    else:
                        say("Not logout")
                        pyautogui.press("enter")
                elif "open" in query:
                    query = query.replace("open ", "")
                    if "website" in query:
                        query = query.replace(" website", "")
                        query = query.replace("website ", "")
                        web.pop(0)
                        web.append(query)
                        # webbrowser.open(f"www.{query}.com")
                    else:
                        if "cutie designer" in query:
                            query = "qt designer"
                        pyautogui.press('win')
                        time.sleep(1)
                        pyautogui.typewrite(f'{query}')
                        time.sleep(1)
                        pyautogui.press('enter')
                elif "close" in query:
                    query = query.replace("close ", "")
                    query = query.lower()[:3]
                    if query == 'wha':
                        query = 'Wha'
                    for proc in psutil.process_iter():
                        try:
                            processName = proc.name()[:3]
                            if processName == query:
                                os.system(f"taskkill /f /im {proc.name()}")
                                break
                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                            pass
                elif "search"in query:
                    query = query.replace("search", "")
                    query = query.replace("on", "")
                    if "wikipedia" in query:
                        say("Sir, what should I search on wikipedia")
                        while True:
                            que = takecom()
                            if "exit" in que or "searching" in que or "stop" in que:
                                say("Exiting...")
                                break
                            elif "none" in que:
                                say("Please sir, tell me what should I search on wikipedia")
                            else:
                                que = que.replace("exit", "")
                                que = que.replace("none", "")
                                results = wikipedia.summary(que, sentences=2)
                                say(f"{que} about {results}")
                                say("Many more information about")
                                say("Tell me yes or no")
                                while True:
                                    bm = takecom()
                                    if "yes" in bm:
                                        results = wikipedia.summary(que, sentences=10)
                                        say(f"okay! many more is {results}")
                                        break
                                    elif "no" in bm:
                                        say("okay! no more information")
                                        break
                                    elif "none" in bm:
                                        say("please sir tell me yes or no")
                    
                    elif "photos" in query:
                        query = query.replace("photos", "")
                        webbrowser.open(f"https://www.google.com/search?q={query}&source=Inms&tbm=isch&sa=X&ved=2ahUKEwjOh-G_ir3zAhV7xzgGHXB5AIAQ_AUoAXoECAEQAw")
                        say(f"There is {query} photos")

                    else:
                        say(f"What should i search on {query}")
                        while True:
                            cm = takecom()
                            if "exit" in cm or "close" in cm or "no search" in cm or "stop" in cm or "stop search" in cm:
                                say("Okay sir, stop searching")
                                break

                            elif "none" in cm:
                                say("Please sir, tell me what should i search on youtube")

                            else:
                                All.search(query, cm)
                                say(f"Searching {query} on {cm}")
                                break
                elif "play" in query:
                    query = query.replace("play", "")
                    kit.playonyt(query)
                    say(f"Enjoy the {query}")
                elif query == "none":
                    continue
                else:
                    try:
                        All.all(query)
                    except Exception as e:
                        print(e)
        except Exception as e:
            say(e)

start = MainThread()
connection = sqlite3.connect('Resources/Database/AiDatabase.db', check_same_thread=False)
cursor = connection.cursor()
now = datetime.datetime.now()
imagesize = QImage(10,10,QImage.Format.Format_ARGB32)
image_scaled = QImage()
imagesize.fill(QColor(255,255,255))

class Welcome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.imageLabel = ImageViewer(QPixmap.fromImage(imagesize))
        self.setCentralWidget(self.imageLabel)
        self.ui = Ui_welcome()
        widget.setWindowTitle("Artificial Assistant")
        self.ui.setupUi(self)
        widget.setFixedHeight(587)
        widget.setFixedWidth(998)
        self.ui.pushButton.clicked.connect(self.get_start)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.get_start)
    def get_start(self):
        width = self.ui.frame.width()
        if width == 0:
            newWidth = 851
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.frame, b"minimumWidth")
        self.animation.setDuration(0)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()
        for i in range(0, 101):
            self.ui.progressBar.setValue(i)
            time.sleep(0.01)
        self.lg = Login_or_register()
        widget.addWidget(self.lg)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Login_or_register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.imageLabel = ImageViewer(QPixmap.fromImage(imagesize))
        self.setCentralWidget(self.imageLabel)
        self.ui = Ui_login_or_register()
        widget.setWindowTitle("Artificial Assistant")
        widget.move(240,40)
        self.ui.setupUi(self)
        widget.setFixedHeight(851)
        widget.setFixedWidth(1401)
        self.ui.pushButton.clicked.connect(self.registration)
        self.ui.pushButton_2.clicked.connect(self.login)
        self.ui.label_4.setPixmap(QtGui.QPixmap("Resources/Images/assistant.gif"))
        self.ui.movie = QMovie("Resources/Images/assistant.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.lg = None
    def registration(self):
        self.rg = Registration()
        widget.addWidget(self.rg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def login(self):
        if self.lg is None:
            self.lg = Login()
            self.lg.show()
        else:
            self.lg.close()
            self.lg = None
        
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.registration)
        self.ui.pushButton_3.clicked.connect(self.fg_passwd)
        self.ui.pushButton_4.clicked.connect(self.cl)
        self.ui.pushButton_5.clicked.connect(self.fg_username)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.login)
        self.fg_ps = None
        self.fg_us = None
        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label_8.mouseMoveEvent = moveWindow
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def cl(self):
        self.hide()
    def login(self):
        user = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()
        if user in "" or passwd in "":
            if user in "":
                self.ui.label_3.setText("Please enter the username")
            
            if passwd in "":
                self.ui.label_4.setText("Please enter the password")
        
        else:
            try:
                cursor.execute('CREATE TABLE Login_info(Username TEXT, Password TEXT, First_name TEXT, Last_name TEXT, Email TEXT, Image BLOB)')
                connection.commit()
            except:
                pass
            cursor.execute(f"SELECT Username FROM Login_info WHERE Username='{user}'")
            us = cursor.fetchone()
            if us == None:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Username does not registered")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
            
            else:
                cursor.execute(f"SELECT Password FROM Login_info WHERE Username='{user}'")
                ps = cursor.fetchone()
                if ps[0] == passwd:
                    msg = QMessageBox()
                    msg.setWindowTitle("Login")
                    msg.setText("Login successfully")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                    self.hide()
                    cursor.execute("INSERT INTO Login VALUES(?, ?)", [user, now])
                    connection.commit()
                    cursor.execute(f"SELECT Email FROM Login_info WHERE Username='{user}'")
                    email = cursor.fetchone()[0]
                    cursor.execute(f"SELECT First_name FROM Login_info WHERE Username='{user}'")
                    name = cursor.fetchone()[0]
                    t = threading.Thread(target=Email_sender.login_sender, args=(email, name))
                    t.start()

                    use.append(user)
                    self.hm = Home()
                    widget.addWidget(self.hm)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Incorrect password")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
    def fg_passwd(self):
        if self.fg_ps is None:
            self.fg_ps = Forget_password()
            self.fg_ps.show()
        else:
            self.fg_ps.close()
            self.fg_ps = None
    def registration(self):
        self.hide()
        self.rg = Registration()
        widget.addWidget(self.rg)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def fg_username(self):
        if self.fg_us is None:
            self.fg_us = Forget_username()
            self.fg_us.show()
        else:
            self.fg_us.close()
            self.fg_us = None

class QrScan(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QrCode()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        widget.setWindowTitle("Artificial Assistant")
        self.ui.pushButton.clicked.connect(self.back)
        self.ui.pushButton_2.clicked.connect(self.browse)
        self.user = use[0]
        self.i = 0
        self.j = 0
        self.k = 0

        self.t = threading.Thread(target=self.camera)
        self.t.start()

        self.other1 = QTimer(self)
        self.other1.timeout.connect(self.other)
        self.other1.start()

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label.mouseMoveEvent = moveWindow

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.j = 1
        self.ui.label_3.setPixmap(QPixmap.fromImage(img))
        self.ui.label_3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def other(self):
        if self.k == 1:
            self.t.join()
            self.login()
            self.other1.stop()

    def camera(self):
        self.cap = cv2.VideoCapture(0)
        myData = ""
        while True:
            success, img = self.cap.read()
            self.displayImage(img, 1)
            if self.j == 1:
                animation1 = QPropertyAnimation(self.ui.label_4, b"geometry")
                animation1.setDuration(0)
                animation1.setEndValue(QRect(230, 300, 0, 51))
                animation1.start()
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(255,0,255),5)
                break
            
            if self.i == 1:
                break

            if myData != "":
                self.myData = myData[5:32]
                cursor.execute(f"SELECT Id FROM Login_info WHERE Username='{self.user}'")
                use_id = cursor.fetchone()[0]
                if use_id == self.myData:
                    self.k = 1
                    break
                else:
                    myData = ""
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Qr Code does not match")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            cv2.waitKey(0)
        self.cap.release()
        cv2.destroyAllWindows()

    def browse(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png *.jpeg)")
        self.file = self.file[0]
        img = cv2.imread(self.file)
        myData = ""

        while True:
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,(255,0,255),5)
                break
            if myData != "":
                self.myData = myData[5:32]
                cursor.execute(f"SELECT Id FROM Login_info WHERE Username='{self.user}'")
                use_id = cursor.fetchone()[0]
                if use_id == self.myData:
                    self.login()
                    self.i = 1
                    break
                else:
                    myData = ""
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Qr Code does not match")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            cv2.waitKey(0)
        self.cap.release()
        cv2.destroyAllWindows()

    def login(self):
        msg = QMessageBox()
        msg.setWindowTitle("Login")
        msg.setText("Login successfully")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        cursor.execute("INSERT INTO Login VALUES(?, ?)", [self.user, now])
        connection.commit()
        self.hide()
        self.hm = Home()
        widget.addWidget(self.hm)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def back(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.login = Login()
        self.login.show()
        self.hide()

class Forget_username(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        widget.setWindowTitle("Artificial Assistant")
        self.ui = Ui_forget_username()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cl)
        self.ui.pushButton_2.clicked.connect(self.send)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.send)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def cl(self):
        self.hide()

    def send(self):
        self.email = self.ui.lineEdit.text()
        if self.email in "":
            self.ui.label_3.setText("Enter the Email address")
        
        else:
            proper = self.email[-10:]
            if proper == "@gmail.com":
                try:
                    cursor.execute(f"SELECT Email FROM Login_info WHERE Email='{self.email}'")
                    em = cursor.fetchone()
                    if em == None:
                        msg = QMessageBox()
                        msg.setWindowTitle("Failed")
                        msg.setText("This email does not registered")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()
                    
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Email send")
                        msg.setText("Email sent successfully")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                        self.hide()
                        t = threading.Thread(target=self.emailsend)
                        t.start()
                        self.hide()

                except:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Email not registered")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Invalid Email address")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def emailsend(self):
        cursor.execute(f"SELECT Username FROM Login_info WHERE Email='{self.email}'")
        us = cursor.fetchone()[0]
        Email_sender.user_sender(self.email, us)

    def back(self):
        self.login = Login()
        self.login.show()
        self.hide()

class Forget_password(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        widget.setWindowTitle("Artificial Assistant")
        self.ui = Ui_forget_password()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cl)
        self.ui.pushButton_2.clicked.connect(self.send)
        self.ui.pushButton_3.clicked.connect(self.back)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.send)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def cl(self):
        self.hide()

    def send(self):
        self.user = self.ui.lineEdit.text()
        self.email = self.ui.lineEdit_2.text()

        if self.user in "" or self.email in "":
            if self.user in "":
                self.ui.label_3.setText("Enter the Username") 
            if self.email in "":
                self.ui.label_4.setText("Enter the Email Address")

        else:
            try:
                cursor.execute(f"SELECT Username FROM Login_info WHERE Username='{self.user}'")
                us = cursor.fetchone()
                if us == None:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Username not registered")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                
                else:
                    proper = self.email[-10:]
                    if proper == "@gmail.com":
                        cursor.execute(f"SELECT Email FROM Login_info WHERE Username='{self.user}'")
                        em = cursor.fetchone()[0]
                        if em == self.email:
                            msg = QMessageBox()
                            msg.setWindowTitle("Successful")
                            msg.setText("Password send successfully")
                            msg.setIcon(QMessageBox.Information)
                            msg.exec_()
                            self.hide()
                            t = threading.Thread(target=self.sendemail)
                            t.start()
                            self.hide()
                        
                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Failed")
                            msg.setText("Email address not match")
                            msg.setIcon(QMessageBox.Critical)
                            msg.exec_()
                    
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Failed")
                        msg.setText("Invalid email address")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()
            
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Username not registered")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def sendemail(self):
        cursor.execute(f"SELECT Password FROM Login_info WHERE Email='{self.email}'")
        passwd = cursor.fetchone()[0]
        Email_sender.pass_sender(self.email, self.user, passwd)

    def back(self):
        self.login = Login()
        self.login.show()
        self.hide()

class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_registration()
        widget.setWindowTitle("Artificial Assistant")
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send)
        self.ui.pushButton_2.clicked.connect(self.cap)
        self.ui.pushButton_3.clicked.connect(self.next)
        self.ui.pushButton_4.clicked.connect(self.sign)
        self.ui.pushButton_5.clicked.connect(self.send)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.next)
        self.cp = None

        self.defaultpath = "Resources/Images/defaultperson.jpg"
        self.ui.label_11.setPixmap(QtGui.QPixmap(self.defaultpath))
        self.image = open(f"{self.defaultpath}", "rb")

        img = QTimer(self)
        img.timeout.connect(self.Pictu)
        img.start()

    def Pictu(self):
        try:
            try:
                if pics[1] != "":
                    pics.pop(0)
            except:
                pass
            self.file = pics[0]
            self.ui.label_11.setPixmap(QtGui.QPixmap(self.file))
            self.image = open(f"{self.file}", "rb")
        except:
            pass

    def send(self):
        email = self.ui.lineEdit_4.text()
        if email in "":
            self.ui.label_7.setText("Please enter the email")
        
        else:
            find = None
            try:
                cursor.execute(f"SELECT Email FROM Login_info WHERE Email='{email}'")
                find = cursor.fetchone()
            except:
                pass
            if find == None:
                try:
                    proper = email[-10:]
                    if proper == "@gmail.com":
                        animation = QPropertyAnimation(self.ui.frame, b"geometry")
                        animation.setDuration(0)
                        animation.setStartValue(QRect(580, 380, 91, 31))
                        animation.setEndValue(QRect(580, 380, 0, 31))
                        animation.start()
                        animation1 = QPropertyAnimation(self.ui.frame_2, b"geometry")
                        animation1.setDuration(0)
                        animation1.setStartValue(QRect(580, 380, 0, 31))
                        animation1.setEndValue(QRect(580, 380, 111, 31))
                        animation1.start()
                        animation2 = QPropertyAnimation(self.ui.frame_3, b"geometry")
                        animation2.setDuration(0)
                        animation2.setStartValue(QRect(0, 0, 0, 31))
                        animation2.setEndValue(QRect(0, 0, 111, 31))
                        animation2.start()
                        animation3 = QPropertyAnimation(self.ui.frame_4, b"geometry")
                        animation3.setDuration(0)
                        animation3.setStartValue(QRect(580, 380, 91, 31))
                        animation3.setEndValue(QRect(580, 380, 0, 31))
                        animation3.start()

                        self.i = 30
                        self.email = email
                        self.timer = QTimer(self)
                        self.timer.timeout.connect(self.showText)
                        self.timer.start(1000)
                        self.otp = generateOTP()
                        t = threading.Thread(target=Email_sender.sender, args=(self.email, self.otp))
                        t.start()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Failed")
                        msg.setText("Invalid email address")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()
                
                except:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Something went wrong")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Email already exist")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def showText(self):
        self.ui.label_12.setText(f"Resend {self.i} sec")
        if self.i == 0:
            self.timer.stop()
            animation = QPropertyAnimation(self.ui.frame_3, b"geometry")
            animation.setDuration(0)
            animation.setStartValue(QRect(0, 0, 111, 31))
            animation.setEndValue(QRect(0, 0, 0, 31))
            animation.start()
            animation2 = QPropertyAnimation(self.ui.frame_4, b"geometry")
            animation2.setDuration(0)
            animation2.setStartValue(QRect(0, 0, 0, 31))
            animation2.setEndValue(QRect(0, 0, 91, 31))
            animation2.start()
            self.ui.label_12.setText(f"Resend 30 sec")
        self.i = self.i - 1

    def cap(self):
        if self.cp is None:
            self.cp = Capture()
            self.cp.show()
        else:
            self.cp.close()
            self.cp = None

    def next(self):
        f_name = self.ui.lineEdit.text()
        l_name = self.ui.lineEdit_2.text()
        user = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_4.text()
        otp1 = self.ui.lineEdit_5.text()
        passwd = self.ui.lineEdit_6.text()
        repasswd = self.ui.lineEdit_7.text()
        image = self.image

        if f_name in "" or l_name in "" or user in "" or email in "" or otp1 in "" or passwd in "" or repasswd in "" or passwd != repasswd:
            if f_name in "":
                self.ui.label_4.setText("Please enter First name")
            if l_name in "":
                self.ui.label_5.setText("Please enter Last name")
            if user in "":
                self.ui.label_6.setText("Please enter Username")
            if email in "":
                self.ui.label_7.setText("Please enter Email")
            if otp1 in "":
                self.ui.label_8.setText("Please enter OTP")
            if passwd in "":
                self.ui.label_9.setText("Please enter Password")
            if repasswd in "":
                self.ui.label_10.setText("Please enter Re-password")
            if passwd != repasswd:
                self.ui.label_9.setText("Both are not same")
                self.ui.label_10.setText("Both are not same")
        
        else:
            self.ui.label_4.setText("")
            self.ui.label_5.setText("")
            self.ui.label_6.setText("")
            self.ui.label_7.setText("")
            self.ui.label_8.setText("")
            self.ui.label_9.setText("")
            self.ui.label_10.setText("")

            try:
                cursor.execute("CREATE TABLE Login_info(Username TEXT, Password TEXT, First_name TEXT, Last_name TEXT, Email TEXT, Image BLOB)")
                connection.commit()
            except:
                pass

            cursor.execute(f"SELECT Username FROM Login_info WHERE Username='{user}'")
            one = cursor.fetchone()
        
            if one == None:
                cursor.execute(f"SELECT Email FROM Login_info")
                two = cursor.fetchall()
                t = 0
                for two1 in two:
                    if two1[0] == email:
                        t = 1
                if t == 1:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Email already exist")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()

                else:
                    if self.otp == otp1:
                        image = sqlite3.Binary(image.read())
                        user_info = [user, repasswd, f_name, l_name, email, image]
                        cursor.execute("INSERT INTO Login_info VALUES(?, ?, ?, ?, ?, ?)", user_info)
                        connection.commit()
                        msg = QMessageBox()
                        msg.setWindowTitle("Registration")
                        msg.setText("Registration successfully")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                        self.lg = Login_or_register()
                        widget.addWidget(self.lg)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        t = threading.Thread(target=Email_sender.register_sender, args=(email, f_name))
                        t.start()
                    
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Failed")
                        msg.setText("Wrong OTP")
                        msg.setIcon(QMessageBox.Critical)
                        msg.exec_()
            
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Username already exist")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def sign(self):
        self.lg = Login_or_register()
        widget.addWidget(self.lg)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Capture(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Capture()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.browse)
        self.ui.pushButton_2.clicked.connect(self.capture)
        self.ui.pushButton_3.clicked.connect(self.cl)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label_2.mouseMoveEvent = moveWindow
    
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def browse(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png *.jpeg)")
        self.file = self.file[0]
        if len(self.file) == 0:
            pics.append(pics[0])
        else:
            pics.append(self.file)
            self.hide()

    def capture(self):
        self.cm = Camera()
        self.cm.show()
        self.hide()

    def cl(self):
        self.hide()

class Camera(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Camera()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cl)
        self.ui.pushButton_2.clicked.connect(self.cap)
        self.i = 0
        self.j = 0
        self.k = 0
        self.a = 0

        self.t = threading.Thread(target=self.camera)
        self.t.start()

        self.st = QTimer(self)
        self.st.timeout.connect(self.sto)
        self.st.start()

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label_3.mouseMoveEvent = moveWindow
    
    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.j = 1
        self.ui.label.setPixmap(QPixmap.fromImage(img))
        self.ui.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def sto(self):
        if self.a == 1:
            self.t.join()
            pics.append("Resources/Images/Capture.png")
            self.hide()
            self.st.stop()

    def camera(self):
        cam = cv2.VideoCapture(0)
        while True:
            res, img = cam.read()
            self.displayImage(img, 1)
            if self.j == 1:
                animation1 = QPropertyAnimation(self.ui.label_2, b"geometry")
                animation1.setDuration(0)
                animation1.setEndValue(QRect(210, 240, 0, 51))
                animation1.start()

            if self.k == 1:
                cv2.imwrite("Resources/Images/Capture.png", img)
                self.a = 1
                break

            if self.i == 1:
                break
            cv2.waitKey(0)
        cam.release()
        cv2.destroyAllWindows()

    def cap(self):
        self.k = 1
        
    def cl(self):
        self.hide()
        self.i = 1

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        self.imageLabel = ImageViewer(QPixmap.fromImage(imagesize))
        self.setCentralWidget(self.imageLabel)
        self.ui = Ui_home()
        self.ui.setupUi(self)
        widget.setFixedHeight(851)
        widget.setFixedWidth(1401)
        widget.move(240,40)
        widget.setWindowTitle("Artificial Assistant")
        self.ui.pushButton.clicked.connect(self.profile)
        self.ui.pushButton_2.clicked.connect(self.menu)
        self.ui.pushButton_3.clicked.connect(self.start)
        self.ui.pushButton_4.clicked.connect(self.logout)
        self.ui.pushButton_5.clicked.connect(self.home)
        self.ui.pushButton_6.clicked.connect(self.profile)
        self.ui.pushButton_7.clicked.connect(self.quit)
        self.ui.pushButton_8.clicked.connect(self.feature)
        self.ui.pushButton_9.clicked.connect(self.launch1)
        self.ui.pushButton_10.clicked.connect(self.back)
        self.ui.pushButton_11.clicked.connect(self.launch2)
        self.ui.pushButton_12.clicked.connect(self.launch3)
        self.ui.pushButton_13.clicked.connect(self.feature)
        self.ui.pushButton_14.clicked.connect(self.clear)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.start)
        web.clear()
        web.append(1)
        clth.append(0)

        self.ui.label_4.setPixmap(QtGui.QPixmap("Resources/Images/initial.gif"))
        self.ui.label_6.setPixmap(QtGui.QPixmap("Resources/Images/Iron_Template_1.gif"))
        self.ui.label_11.setPixmap(QtGui.QPixmap("Resources/Images/Earth.gif"))
        self.ui.label_5.setPixmap(QtGui.QPixmap("Resources/Images/Aqua.gif"))
        self.ui.label_9.setPixmap(QtGui.QPixmap("Resources/Images/wdwdwd.png"))
        self.ui.label_2.setPixmap(QtGui.QPixmap("Resources/Images/menu.png"))
        self.ui.label_3.setPixmap(QtGui.QPixmap("Resources/Images/defaultperson.jpg"))

        self.user = use[0]

        cursor.execute(f"SELECT Image FROM Login_info WHERE Username='{self.user}'")
        image = cursor.fetchone()[0]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg')
        self.ui.label_3.setPixmap(pixmap)
        self.ui.label_13.setPixmap(pixmap)

        timer = QTimer(self)
        timer.timeout.connect(self.showText)
        timer.start(1000)
        other = QTimer(self)
        other.timeout.connect(self.other)
        other.start()
        tm.append(0)
        self.sp = None
        self.ln1 = None
        self.ln2 = None
        self.ln3 = None
        
    def other(self):

        width = self.ui.frame.width()
        if width == 0:
            self.ui.label_2.setPixmap(QtGui.QPixmap("Resources/Images/menu.png"))
        else:
            self.ui.label_2.setPixmap(QtGui.QPixmap("Resources/Images/menu2.png"))

        for take in tk:
            text = f"{self.user} : {take}\n"
            self.TextEdit(text)
            tk.remove(take)
        for say in sp:
            text = f"Assistant : {say}\n"
            self.TextEdit(text)
            sp.remove(say)
        for pr in ls:
            self.ui.label_8.setText(pr)
            ls.remove(pr)
        
        if web[0] == 1:
            pass
        else:
            self.bt = Browser1(web[0])
            self.bt.show()
            web.pop(0)
            web.append(1)

        if tm[0] == 1:
            tm.pop(0)
            self.profile()
            tm.append(0)
        if tm[0] == 2:
            self.home()
            tm.pop(0)
            tm.append(0)
        if tm[0] == 3:
            self.feature()
            tm.pop(0)
            tm.append(0)
        if tm[0] == 4:
            self.quit()
            tm.pop(0)
            tm.append(0)
        if tm[0] == 5:
            self.logout()
            tm.pop(0)
            tm.append(0)
        if tm[0] == 8:
            tm.pop(0)
            self.back()
            tm.append(0)
        if tm[0] == 9:
            tm.pop(0)
            self.hide()
            tm.append(0)
        if tm[0] == 10:
            tm.pop(0)
            self.show()
            tm.append(0)

    def showText(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label_16.setText(label_time)
        self.ui.label_17.setText(label_date)
        cursor.execute(f"SELECT Image FROM Login_info WHERE Username='{self.user}'")
        image = cursor.fetchone()[0]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image, 'jpg, png')
        self.ui.label_3.setPixmap(pixmap)
        self.ui.label_13.setPixmap(pixmap)
        cursor.execute(f"SELECT First_name FROM Login_info WHERE Username='{self.user}'")
        f_name = cursor.fetchone()
        cursor.execute(f"SELECT Last_name FROM Login_info WHERE Username='{self.user}'")
        l_name = cursor.fetchone()
        f_name = f_name[0].upper()
        l_name = l_name[0].upper()
        self.ui.label_14.setText(f"{f_name}")
        self.ui.label_15.setText(f"{l_name}")

    def TextEdit(self, text):
        cur = self.ui.textEdit.textCursor()
        cur.movePosition(QtGui.QTextCursor.End)
        cur.insertText(text)
        if self.ui.textEdit.document().lineCount() > 16:
            cur.movePosition(QtGui.QTextCursor.Start)
            cur.select(QtGui.QTextCursor.LineUnderCursor)
            cur.removeSelectedText()
            cur.deleteChar()
        self.ui.textEdit.ensureCursorVisible()

    def profile(self):
        if self.sp is None:
            self.sp = ShowProfile()
            self.sp.show()
        else:
            self.sp.close()
            self.sp = None 
        width = self.ui.frame.width()
        if width == 251:
            newWidth = 0
        else:
            newWidth = 0
        self.animation1 = QPropertyAnimation(self.ui.frame, b"maximumWidth")
        self.animation1.setDuration(250)
        self.animation1.setStartValue(width)
        self.animation1.setEndValue(newWidth)
        self.animation1.start()

    def menu(self):
        width = self.ui.frame.width()
        if width == 0:
            newWidth = 251
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()

    def start(self):
        self.ui.movie = QMovie("Resources/Images/initial.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QMovie("Resources/Images/Iron_Template_1.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QMovie("Resources/Images/Earth.gif")
        self.ui.label_11.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QMovie("Resources/Images/Aqua.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        start.start()

    def logout(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure ?")
        msgBox.setWindowTitle("Logout")
        msgBox.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        msgBox.setDefaultButton(QMessageBox.No)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Yes:
            self.lg = Login_or_register()
            widget.addWidget(self.lg)
            widget.setCurrentIndex(widget.currentIndex()+1)
            use.remove(self.user)
            cursor.execute("INSERT INTO Login VALUES(?, ?)", ["logout", now])
            connection.commit()

    def home(self):
        width = self.ui.frame.width()
        if width == 251:
            newWidth = 0
        else:
            newWidth = 0
        self.animation1 = QPropertyAnimation(self.ui.frame, b"maximumWidth")
        self.animation1.setDuration(250)
        self.animation1.setStartValue(width)
        self.animation1.setEndValue(newWidth)
        self.animation1.start()
        animation = QPropertyAnimation(self.ui.frame_3, b"geometry")
        animation.setDuration(0)
        animation.setStartValue(QRect(0, 40, 1401, 811))
        animation.setEndValue(QRect(0, 40, 0, 811))
        animation.start()

    def quit(self):
        width = self.ui.frame.width()
        if width == 0:
            newWidth = 0
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure ?")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Close | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Close:
            say("Thankyou for using me sir, have a good day")
            exit()

    def feature(self):
        width = self.ui.frame.width()
        if width == 250:
            newWidth = 0
        else:
            newWidth = 0
        self.animation = QPropertyAnimation(self.ui.frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.start()
        animation1 = QPropertyAnimation(self.ui.frame_3, b"geometry")
        animation1.setDuration(0)
        animation1.setStartValue(QRect(0, 40, 0, 811))
        animation1.setEndValue(QRect(0, 40, 1401, 811))
        animation1.start()

    def launch1(self):
        if self.ln1 is None:
            self.ln1 = Add_application()
            self.ln1.show()
        else:
            self.ln1.close()
            self.ln1 = None 

    def back(self):
        animation = QPropertyAnimation(self.ui.frame_3, b"geometry")
        animation.setDuration(0)
        animation.setStartValue(QRect(0, 0, 1401, 851))
        animation.setEndValue(QRect(0, 0, 0, 851))
        animation.start()

    def launch2(self):
        if self.ln2 is None:
            self.ln2 = Mouse()
            self.ln2.show()
        else:
            self.ln2.close()
            self.ln2 = None 

    def launch3(self):
        if self.ln3 is None:
            self.ln3 = Browser()
            self.ln3.show()
        else:
            self.ln3.close()
            self.ln3 = None

    def clear(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure ?")
        msgBox.setWindowTitle("Clear all data")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            cursor.close()
            connection.close()
            self.wc = Welcome()
            widget.addWidget(self.wc)
            widget.setCurrentIndex(widget.currentIndex()+1)
            os.remove('Resources/Database/AiDatabase.db')
            exit()

class Browser1(QMainWindow):
    def __init__(self, website):
        super(QMainWindow, self).__init__()
        self.imageLabel = ImageViewer(QPixmap.fromImage(imagesize))
        self.setCentralWidget(self.imageLabel)
        self.browser = QWebEngineView()
        self.website = website
        self.browser.setUrl(QUrl(f"https://{self.website}.com"))
        self.setCentralWidget(self.browser)
        self.resize(1200, 700)
        self.show()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back = QtGui.QPixmap("back.png")
        back_btn.setIcon(QtGui.QIcon(back))
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward = QtGui.QPixmap("forward.png")
        forward_btn.setIcon(QtGui.QIcon(forward))
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn
        home = QtGui.QPixmap("home.png")
        home_btn.setIcon(QtGui.QIcon(home))
        home_btn .triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

class ShowProfile(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_ShowProfile()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.edit)
        self.ui.pushButton_2.clicked.connect(self.cl)
        self.user = use[0]
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.edit)
        auto = QTimer(self)
        auto.timeout.connect(self.Auto)
        auto.start()
        self.ed = None

        cursor.execute(f"SELECT Image FROM Login_info WHERE Username='{self.user}'")
        self.image = cursor.fetchone()[0]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.image, 'jpg, png')
        self.ui.label.setPixmap(pixmap)
        cursor.execute(f"SELECT Username FROM Login_info WHERE Username='{self.user}'")
        user = cursor.fetchone()[0]
        cursor.execute(f"SELECT First_name FROM Login_info WHERE Username='{self.user}'")
        f_name = cursor.fetchone()[0]
        cursor.execute(f"SELECT Last_name FROM Login_info WHERE Username='{self.user}'")
        l_name = cursor.fetchone()[0]
        cursor.execute(f"SELECT Email FROM Login_info WHERE Username='{self.user}'")
        email = cursor.fetchone()[0]
        self.ui.lineEdit.setText(f"{user}")
        self.ui.lineEdit_2.setText(f"{f_name}")
        self.ui.lineEdit_3.setText(f"{l_name}")
        self.ui.lineEdit_4.setText(f"{email}")

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label_3.mouseMoveEvent = moveWindow

    def Auto(self):
        if tm[0] == 6:
            self.cl()
            tm.pop(0)
            tm.append(0)
        elif tm[0] == 7:
            self.edit()
            tm.pop(0)
            tm.append(0)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def edit(self):
        if self.ed is None:
            self.ed = EditProfile()
            self.ed.show()
            self.hide()
        else:
            self.ed.close()
            self.ed = None

    def cl(self):
        self.hide()

class EditProfile(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_EditProfile()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.browse)
        self.ui.pushButton_2.clicked.connect(self.send)
        self.ui.pushButton_3.clicked.connect(self.bc)
        self.ui.pushButton_4.clicked.connect(self.save)
        self.ui.pushButton_5.clicked.connect(self.cl)

        self.user = use[0]
        cursor.execute(f"SELECT Image FROM Login_info WHERE Username='{self.user}'")
        self.image = cursor.fetchone()[0]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(self.image, 'jpg, png')
        self.ui.label_2.setPixmap(pixmap)
        cursor.execute(f"SELECT Username FROM Login_info WHERE Username='{self.user}'")
        user = cursor.fetchone()[0]
        cursor.execute(f"SELECT First_name FROM Login_info WHERE Username='{self.user}'")
        f_name = cursor.fetchone()[0]
        cursor.execute(f"SELECT Last_name FROM Login_info WHERE Username='{self.user}'")
        l_name = cursor.fetchone()[0]
        cursor.execute(f"SELECT Email FROM Login_info WHERE Username='{self.user}'")
        email = cursor.fetchone()[0]
        self.ui.lineEdit.setText(f"{user}")
        self.ui.lineEdit_2.setText(f"{f_name}")
        self.ui.lineEdit_3.setText(f"{l_name}")
        self.ui.lineEdit_4.setText(f"{email}")

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label_3.mouseMoveEvent = moveWindow

    def browse(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png *.jpeg)")
        self.file = self.file[0]
        if len(self.file) == 0:
            cursor.execute(f"SELECT Image FROM Login_info WHERE Username='{self.user}'")
            image = cursor.fetchone()[0]
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image, 'jpg')
            self.ui.label_2.setPixmap(pixmap)
        else:
            self.ui.label_2.setPixmap(QtGui.QPixmap(self.file))
            self.image = open(f"{self.file}", "rb")

    def send(self):
        self.email = self.ui.lineEdit_4.text()
        if self.email in "":
            self.ui.label_4.setText("Please enter the email")
       
        else: 
            try:
                proper = self.email[-10:]
                if proper == "@gmail.com":
                    self.setFixedHeight(660)
                    animation = QPropertyAnimation(self.ui.frame, b"geometry")
                    animation.setDuration(0)
                    animation.setEndValue(QRect(80, 500, 491, 61))
                    animation.start()
                    animation1 = QPropertyAnimation(self.ui.frame_2, b"geometry")
                    animation1.setDuration(0)
                    animation1.setEndValue(QRect(130, 580, 381, 41))
                    animation1.start()
                    animation2 = QPropertyAnimation(self.ui.frame_3, b"geometry")
                    animation2.setDuration(0)
                    animation2.setEndValue(QRect(220, 0, 0, 41))
                    animation2.start()
                    animation3 = QPropertyAnimation(self.ui.frame_4, b"geometry")
                    animation3.setDuration(0)
                    animation3.setEndValue(QRect(0, 0, 0, 31))
                    animation3.start()
                    animation4 = QPropertyAnimation(self.ui.frame_6, b"geometry")
                    animation4.setDuration(0)
                    animation4.setEndValue(QRect(0, 0, 121, 31))
                    animation4.start()
                    self.i = 29
                    self.timer = QTimer(self)
                    self.timer.timeout.connect(self.second)
                    self.timer.start(1000)

                    t = threading.Thread(target=self.sendemail)
                    t.start()
                    
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Invalid email address")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            
            except Exception as e:
                print(e)
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Something went wrong")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def sendemail(self):
        self.otp = generateOTP()
        Email_sender.sender(self.email, self.otp)

    def second(self):
        self.ui.label_5.setText(f"Resend {self.i} sec")
        if self.i == -1:
            self.timer.stop()
            animation = QPropertyAnimation(self.ui.frame_6, b"geometry")
            animation.setDuration(0)
            animation.setEndValue(QRect(0, 0, 0, 31))
            animation.start()
            animation2 = QPropertyAnimation(self.ui.frame_4, b"geometry")
            animation2.setDuration(0)
            animation2.setEndValue(QRect(0, 0, 121, 31))
            animation2.start()
            self.ui.label_5.setText(f"Resend 30 sec")
        self.i = self.i - 1

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def bc(self):
        self.sh = ShowProfile()
        self.sh.show()
        self.hide()

    def save(self):
        f_name = self.ui.lineEdit_2.text()
        l_name = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_4.text()
        otp1 = self.ui.lineEdit_5.text()

        if f_name in "" or l_name in "" or email in "" or otp1 in "":
            if f_name in "":
                self.ui.label_7.setText("Enter the First name")
            if l_name in "":
                self.ui.label_8.setText("Enter the Last name")
            if email in "":
                self.ui.label_4.setText("Enter the Email address")
            if otp1 in "":
                self.ui.label_6.setText("Enter the OTP")
        else:
            self.ui.label_7.setText("")
            self.ui.label_8.setText("")
            self.ui.label_4.setText("")
            self.ui.label_6.setText("")
            if self.otp == otp1:
                image = self.image
                try:
                    cursor.execute(f"UPDATE Login_info SET Image = ? WHERE Username = '{self.user}'", [sqlite3.Binary(image.read())])
                    connection.commit()
                except Exception as e:
                    print(e)
                cursor.execute(f"UPDATE Login_info SET First_name = ? WHERE Username = '{self.user}'", [f_name])
                connection.commit()
                cursor.execute(f"UPDATE Login_info SET Last_name = ? WHERE Username = '{self.user}'", [l_name])
                connection.commit()
                cursor.execute(f"UPDATE Login_info SET Email = ? WHERE Username = '{self.user}'", [email])
                connection.commit()
                msg = QMessageBox()
                msg.setWindowTitle("Saved")
                msg.setText("Update successfully")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                self.hide()

    def cl(self):
        self.hide()

class Add_application(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Add()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cl)
        self.ui.pushButton_2.clicked.connect(self.browse)
        self.ui.pushButton_3.clicked.connect(self.add)
        self.ui.pushButton_4.clicked.connect(self.help)
        self.enter = QShortcut(QKeySequence('Enter'), self)
        self.enter.activated.connect(self.add)

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label_4.mouseMoveEvent = moveWindow
    
    def help(self):
        self.hp = Add_help()
        self.hp.show()

    def cl(self):
        self.hide()

    def browse(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"EXE files (*.exe)")
        self.file = self.file[0]
        self.ui.lineEdit_2.setText(self.file)

    def add(self):
        name = self.ui.lineEdit.text()
        path = self.ui.lineEdit_2.text()
        if name in "" or path in "":
            if name in "":
                self.ui.label.setText("Please enter the name")
            if path in "":
                self.ui.label_2.setText("Please choose the path")
        
        else:
            self.ui.label.setText("")
            self.ui.label_2.setText("")
            extension = path[-4:]
            if extension == ".exe":
                path = path.replace("/", "\\")
                cursor.execute(f"SELECT Path FROM Application WHERE Path='{path}'")
                found = cursor.fetchone()
                if found == None:
                    all = [name, path]
                    cursor.execute("INSERT INTO Application VALUES(?, ?)", all)
                    connection.commit()
                    msg = QMessageBox()
                    msg.setWindowTitle("Saved")
                    msg.setText("Save successfully")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Failed")
                    msg.setText("Already exists")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText("Application path not found")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

class Add_help(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Add_help()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.cl)

        self.ui.label_3.setPixmap(QtGui.QPixmap("Resources/Images/1.png"))
        self.ui.label_5.setPixmap(QtGui.QPixmap("Resources/Images/2.png"))
        self.ui.label_7.setPixmap(QtGui.QPixmap("Resources/Images/3.png"))
        self.ui.label_9.setPixmap(QtGui.QPixmap("Resources/Images/4.png"))

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def cl(self):
        self.hide()

class Mouse(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_Mouse()
        self.ui.setupUi(self)
        self.i = 0
        self.j = 0
        self.ui.pushButton.clicked.connect(self.cl)

        t2 = threading.Thread(target=self.mouse)
        t2.start()

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.label.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def cl(self):
        say("Now camera is closing...")
        self.i = 1
        self.hide()
        self.cap.release()
        cv2.destroyAllWindows()

    def mouse(self):
        say("Please wait sir, Opening a camera")
        wCam, hCam = 640, 480
        frameR = 100
        smoothening = 7

        pTime = 0
        plocX, plocY = 0, 0
        clocX, clocY = 0, 0
    
        self.cap = cv2.VideoCapture(0)
        
        self.cap.set(3, wCam)
        self.cap.set(4, hCam)
        detector = htm.handDetector(maxHands=1)
        wScr, hScr = autopy.screen.size()
        print(wScr, hScr)

        while True:
            if self.i == 1:
                print("Stop")
                break
            else:
                success, img = self.cap.read()
                img = detector.findHands(img)
                lmList, bbox = detector.findPosition(img)

                if self.j == 1:
                    animation1 = QPropertyAnimation(self.ui.label_5, b"geometry")
                    animation1.setDuration(0)
                    animation1.setStartValue(QRect(290, 230, 131, 41))
                    animation1.setEndValue(QRect(290, 230, 0, 41))
                    animation1.start()
                if len(lmList)!=0:
                    x1, y1 = lmList[8][1:]
                    x2, y2 = lmList[12][1:]
                    fingers = detector.fingersUp()
                    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

                    if fingers[1] == 1 and fingers[2] == 0:

                        x3 = np.interp(x1, (frameR, wCam - frameR), (0,wScr))
                        y3 = np.interp(y1, (frameR, hCam - frameR), (0,hScr))

                        clocX = plocX + (x3 - plocX) / smoothening
                        clocY = plocY + (y3 - plocY) / smoothening

                        autopy.mouse.move(wScr - clocX, clocY)
                        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                        plocX, plocY = clocX, clocY

                    if fingers[1] == 1 and fingers[2] == 1:
                        length, img, lineInfo = detector.findDistance(8, 12, img)
                        if length < 40:
                            cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 255), cv2.FILLED)
                            autopy.mouse.click()

                cTime = time.time()
                fps = 1/(cTime-pTime)
                pTime = cTime
                cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

                self.displayImage(img, 1)
                cv2.waitKey()
        self.cap.release()
        cv2.destroyAllWindows()

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if (img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        self.j = 1
        self.ui.label_4.setPixmap(QPixmap.fromImage(img))
        self.ui.label_4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

class Browser(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.imageLabel = ImageViewer(QPixmap.fromImage(imagesize))
        self.setCentralWidget(self.imageLabel)
        self.browser = QWebEngineView()
        self.resize(1200, 500)
        self.setWindowTitle("Artificial Assistant")
        self.browser.setUrl(QUrl("https://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn .triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
        self.show()

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Artificial Assistant")
widget = QtWidgets.QStackedWidget()

try:
    cursor.execute("CREATE TABLE Login(Username TEXT, DateTime TEXT)")
    connection.commit()
except:
    pass

try:
    cursor.execute("SELECT Username FROM Login")
    all = cursor.fetchall()[-1]
    if all[0] == "logout":
        wc = Login_or_register()
    else:
        cursor.execute("INSERT INTO Login VALUES(?, ?)", [all[0], now])
        connection.commit()
        use.append(all[0])
        wc = Home()
except Exception as e:
    print(e)
    wc = Welcome()

widget.addWidget(wc)
widget.show()

app.lastWindowClosed.connect(close_thread)

try:
    sys.exit(app.exec_())
except:
    pass