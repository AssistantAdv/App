# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Camera.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Camera(object):
    def setupUi(self, Camera):
        Camera.setObjectName("Camera")
        Camera.resize(579, 579)
        Camera.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(Camera)
        self.label.setGeometry(QtCore.QRect(50, 90, 481, 361))
        self.label.setStyleSheet("border:2px solid rgb(121, 121, 121);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Camera)
        self.label_2.setGeometry(QtCore.QRect(210, 240, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:none;\n"
"color:rgb(240, 240, 240);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Camera)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 490, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: rgb(108, 255, 238);\n"
"    border:1px solid rgb(108,255,238);\n"
"    border-bottom-left-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(108,255,238);\n"
"    color:rgb(0,0,0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Camera)
        self.pushButton.setGeometry(QtCore.QRect(510, 0, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"    color:rgb(255,255,255)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Camera)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 581, 41))
        self.label_3.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"border:2px solid rgb(121, 121, 121);\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Camera)
        QtCore.QMetaObject.connectSlotsByName(Camera)

    def retranslateUi(self, Camera):
        _translate = QtCore.QCoreApplication.translate
        Camera.setWindowTitle(_translate("Camera", "Dialog"))
        self.label_2.setText(_translate("Camera", "Please wait..."))
        self.pushButton_2.setText(_translate("Camera", "Capture"))
        self.pushButton.setText(_translate("Camera", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Camera = QtWidgets.QDialog()
    ui = Ui_Camera()
    ui.setupUi(Camera)
    Camera.show()
    sys.exit(app.exec_())
