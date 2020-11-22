# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_2(object):
    def setupUi(self, register_2):
        register_2.setObjectName("register_2")
        register_2.resize(1044, 620)
        register_2.setStyleSheet("background-color:#F3F4F1;\n"
"QFrame\n"
"{\n"
"    background:#333;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(register_2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1024, 600))
        self.frame.setMouseTracking(True)
        self.frame.setStyleSheet("QFrame{\n"
"background:#F3F4F1\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(184, 294, 195, 40))
        self.label.setStyleSheet("QLabel{\n"
"    font: 11pt \"Segoe UI\";\n"
"color: #00648e;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(392, 284, 480, 61))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setTabletTracking(True)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border-color: #00648E;\n"
"border:1px solid #00648E;\n"
"border-radius:15px;\n"
"color:#00648E;\n"
"font:30px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-radius:20px;\n"
"}\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(196, 390, 180, 40))
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 30px \"Segoe UI\";\n"
"color: #00648e;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(392, 380, 480, 61))
        self.lineEdit_2.setMouseTracking(True)
        self.lineEdit_2.setTabletTracking(True)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:15px;\n"
"color:#00648E;\n"
"font:30px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border-radius:15px;\n"
"}\n"
"")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.PushButton = QtWidgets.QPushButton(self.frame)
        self.PushButton.setGeometry(QtCore.QRect(392, 476, 240, 61))
        self.PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PushButton.setStyleSheet("QPushButton{\n"
"    font: 30px \"Ubuntu\";\n"
"background:#00648e;\n"
"color:white;\n"
"border-color: #00000066;\n"
"border:1px solid #00648E;\n"
"border-radius:10px;\n"
"}")
        self.PushButton.setObjectName("PushButton")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(184, 198, 370, 40))
        self.label_3.setStyleSheet("QLabel{\n"
"    font: 75 11pt \"Segoe UI\";\n"
"color: #00648e;\n"
"size:30px;\n"
"\n"
"}")
        self.label_3.setObjectName("label_3")
        f=open("path.txt","r")
        d_path=f.read()
        f.close()
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(400, 52, 223, 115))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(d_path+"/source/Icons/logo_Big-Fat-Display.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(298, 568, 521, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: #F3F4F1;\n"
"color: rgb(0, 100, 142);\n"
"alternate-background-color: #F3F4F1;\n"
"border: 0px;\n"
"gridline-color: #F3F4F1;\n"
"selection-color: #F3F4F1;\n"
"selection-background-color: #F3F4F1;\n"
"font: 16px \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(10, 600, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(1041, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        register_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "MainWindow"))
        self.label.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-size:30px; color:#00648e;\">Customer ID</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("register_2", "   XXXX-XXXX-XXXX"))
        self.label_2.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-size:30px; color:#00648e;\">Software ID</span></p></body></html>"))
        self.lineEdit_2.setPlaceholderText(_translate("register_2", "   XXXX-XXXX-XXXX"))
        self.PushButton.setWhatsThis(_translate("register_2", "<html><head/><body><p><span style=\" color:#ffffff;\">fSfER</span></p></body></html>"))
        self.PushButton.setText(_translate("register_2", "Register"))
        self.label_3.setText(_translate("register_2", "<html><head/><body><p><span style=\" font-size:30px; font-weight:600; color:#00648e;\">Register Your Device</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("register_2", "<html><head/><body><p><span style=\" font-size:16px;\">© 2019 Big Fat Designs, LLC. All rights Reserved. </span><span style=\" font-size:16px; text-decoration: underline;\">Learn More.</span></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("register_2", "<html><head/><body><p><span style=\" font-weight:600;\">© 2019 Big Fat Designs, LLC All rights Reserved. </span><span style=\" font-weight:600; text-decoration: underline;\">Learn More.</span></p></body></html>"))
        self.pushButton.setText(_translate("register_2", "© 2019 Big Fat Designs, LLC. All rights Reserved. Learn More."))

import source_rc
