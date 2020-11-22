# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaunchVdownload.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Launch(object):
    def setupUi(self, Launch):
        Launch.setObjectName("Launch")
        Launch.resize(1044, 620)
        Launch.setStyleSheet("background-color: #F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Launch)
        self.centralwidget.setObjectName("centralwidget")
        f=open("path.txt","r")
        d_path=f.read()
        f.close()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(13, 594, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1024, 600))
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet("QFrame{\n"
"background:#F3F4F1\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.PushButton = QtWidgets.QPushButton(self.frame)
        self.PushButton.setGeometry(QtCore.QRect(174, 259, 240, 120))
        self.PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton.setStyleSheet("QPushButton{\n"
"    font: 57 11pt \"Ubuntu\";\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:10px;\n"
"}")
        self.PushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icon_play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PushButton.setIcon(icon)
        self.PushButton.setIconSize(QtCore.QSize(66, 66))
        self.PushButton.setObjectName("PushButton")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(400, 52, 223, 115))
        self.label_6.setStyleSheet("image: url(:/newPrefix/logo_Big-Fat-Display.svg);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/logo_Big-Fat-Display.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.PushButton_3 = QtWidgets.QPushButton(self.frame)
        self.PushButton_3.setGeometry(QtCore.QRect(174, 360, 240, 130))
        self.PushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_3.setStyleSheet("QPushButton{\n"
"font: 30px \"Segoe UI\";\n"
"\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.PushButton_3.setIconSize(QtCore.QSize(50, 53))
        self.PushButton_3.setObjectName("PushButton_3")
        self.PushButton_4 = QtWidgets.QPushButton(self.frame)
        self.PushButton_4.setGeometry(QtCore.QRect(642, 360, 240, 130))
        self.PushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_4.setStyleSheet("QPushButton{\n"
"font: 18pt \"Ubuntu\";\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"\n"
"border-radius:10px;\n"
"}")
        self.PushButton_4.setIconSize(QtCore.QSize(50, 53))
        self.PushButton_4.setObjectName("PushButton_4")
        self.PushButton_2 = QtWidgets.QPushButton(self.frame)
        self.PushButton_2.setGeometry(QtCore.QRect(642, 259, 240, 120))
        self.PushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton_2.setStyleSheet("QPushButton{\n"
"background:#00648E;\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:10px;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/icon_sync.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PushButton_2.setIcon(icon1)
        self.PushButton_2.setIconSize(QtCore.QSize(68, 89))
        self.PushButton_2.setObjectName("PushButton_2")
        self.pushButton5 = QtWidgets.QPushButton(self.frame)
        self.pushButton5.setGeometry(QtCore.QRect(300, 570, 511, 21))
        self.pushButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton5.setStyleSheet("background-color: #F3F4F1;\n"
"color: rgb(0, 100, 142);\n"
"alternate-background-color: #F3F4F1;\n"
"border: 0px;\n"
"gridline-color: #F3F4F1;\n"
"selection-color: #F3F4F1;\n"
"selection-background-color: #F3F4F1;\n"
"font: 16px \"Segoe UI\";")
        self.pushButton5.setObjectName("pushButton5")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(13, 594, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        Launch.setCentralWidget(self.centralwidget)

        self.retranslateUi(Launch)
        QtCore.QMetaObject.connectSlotsByName(Launch)

    def retranslateUi(self, Launch):
        _translate = QtCore.QCoreApplication.translate
        Launch.setWindowTitle(_translate("Launch", "MainWindow"))
        self.PushButton.setWhatsThis(_translate("Launch", "<html><head/><body><p>fSf</p></body></html>"))
        self.PushButton_3.setWhatsThis(_translate("Launch", "<html><head/><body><p><span style=\" font-size:30px;\">fSf</span></p></body></html>"))
        self.PushButton_3.setText(_translate("Launch", "Launch\n"
"Display"))
        self.PushButton_4.setWhatsThis(_translate("Launch", "<html><head/><body><p>fSf</p></body></html>"))
        self.PushButton_4.setText(_translate("Launch", "Download\n"
"Content"))
        self.PushButton_2.setWhatsThis(_translate("Launch", "<html><head/><body><p>fSf</p></body></html>"))
        self.pushButton5.setToolTip(_translate("Launch", "<html><head/><body><p><span style=\" font-size:16px;\">© 2019 Big Fat Designs, LLC. All rights Reserved. </span><span style=\" font-size:16px; text-decoration: underline;\">Learn More.</span></p></body></html>"))
        self.pushButton5.setWhatsThis(_translate("Launch", "<html><head/><body><p><span style=\" font-weight:600;\">© 2019 Big Fat Designs, LLC All rights Reserved. </span><span style=\" font-weight:600; text-decoration: underline;\">Learn More.</span></p></body></html>"))
        self.pushButton5.setText(_translate("Launch", "© 2019 Big Fat Designs, LLC. All rights Reserved. Learn More."))

import source_rc
