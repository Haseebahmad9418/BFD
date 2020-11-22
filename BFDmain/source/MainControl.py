from PyQt5 import QtCore, QtGui, QtWidgets
#import PyQt5.QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon
import os,sys
import glob
import json
import threading
import time
from Image import Ui_MainWindow
import datetime
#import Video_Player
from Video_PlayerVLC import Ui_VideoWindow
##from Video_Player import VideoWindow
from PyQt5.QtWidgets import QFrame
import vlc
from collections import OrderedDict
global curframe
curframe=0
with open('json_received.json') as f:
    data = json.load(f)
                
Cat = []                    
for t in data:
    Cat.append(t['CATTITLE'])
    print("File_name['CATTITLE']", t['CATTITLE'])

tabdata = list(OrderedDict.fromkeys(Cat))
global TabName
TabName = None
global check
check= True

class Ui_ControlWindow(object):
    directoryPath = ""
    UUID = []
    content_title = []
    def setupUi(self, ControlWindow):
        self.getPath()
        ControlWindow.setObjectName("ControlWindow")
        ControlWindow.setWindowModality(QtCore.Qt.NonModal)
        ControlWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        ControlWindow.resize(1024, 631)
        ControlWindow.setMinimumSize(QtCore.QSize(1024, 631))
        ControlWindow.setMaximumSize(QtCore.QSize(1024, 631))
        ControlWindow.setStyleSheet("palette.setColor(QtGui.QPalette.Background, QColor(\"#99ccff\"));")
        self.centralwidget = QtWidgets.QWidget(ControlWindow)

        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 631))
        self.frame.setStyleSheet("background-color: rgb(243, 244, 241); border: 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 220, 1026, 413))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)                    
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
                                     "    alignment: center;\n"
                                     "    background-color: #00648E;\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget::item:selected {\n"
                                     "    border: 0px solid rgb(253, 136, 0);\n"
                                     "    padding: 0px;\n"
                                     "}\n"
                                     "\n"
                                     "QTabWidget>QWidget>QWidget{\n"
                                     "    border: 0px;\n"
                                     "background: #00648E;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab {\n"
                                     "    background: #B2B2B2;\n"
                                     "    border: 0px;\n"
                                     "    border-top-left-radius: 20px;\n"
                                     "    border-top-right-radius: 20px;\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    min-width: 120px;\n"
                                     "    min-height:30px;\n"
                                     "    padding: 10px 50px 10px 50px;\n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                                     "    border: 0px;\n"
                                     "    background: #00648E;\n"
                                     "    \n"
                                     "}\n"
                                     "\n"
                                     "QTabBar::tab:selected {\n"
                                     "    border: 0px;\n"
                                     "}")
        
        self.tabWidget.setIconSize(QtCore.QSize(180, 180))
        self.tabWidget.setObjectName("tabWidget")
        self.uiV = Ui_VideoWindow()


        self.thumbnail_entries = os.listdir(self.directoryPath + '/data/Thumbnails')
        self.data_entries = os.listdir(self.directoryPath + '/data/Content')

        self.left_button = QtWidgets.QPushButton(self.frame)
        self.left_button.setGeometry(QtCore.QRect(20, 20, 61, 151))
        self.left_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("l.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_button.setIcon(icon)
        self.left_button.setStyleSheet("border: 0px;\n")
        self.left_button.setIconSize(QtCore.QSize(200, 170))
        self.left_button.setObjectName("left_button")
        self.right_button = QtWidgets.QPushButton(self.frame)
        self.right_button.setGeometry(QtCore.QRect(950, 20, 61, 151))
        self.right_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.right_button.setStyleSheet("border: 0px;\n")
        self.right_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("r.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_button.setIcon(icon1)
        self.right_button.setIconSize(QtCore.QSize(200, 170))
        self.right_button.setObjectName("right_button")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(500, 20, 100, 48))
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setStyleSheet("background-color: rgb(243, 244, 241);\n"
                                     "border: 0px;\n"
                                     "color: #00648E;\n"
                                        )
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setMaximum(100)

        self.horizontalSlider.setGeometry(QtCore.QRect(200, 60, 600, 150))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
                                            "    border: 0px solid #999999;\n"
                                            "    height: 50px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
                                            "    background: #044763;\n"
                                            "    margin: 0 0;\n"
                                            "    border-radius: 25px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::handle:horizontal {\n"
                                            "    background: qlineargradient( x1:0 y1:0.3, x2:0 y2:1, stop:0 #FD8800, stop:0.54 #DC7600, stop:1 #7F4400);\n"
                                            "    border: 1px solid #5c5c5c;\n"
                                            "    width: 90px;\n"
                                            "    height: 90px;\n"
                                            "    line-height: 90px;\n"
                                            "    margin: -20px 0px; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
                                            "    border-radius: 45px;\n"
                                            "}")
        self.horizontalSlider.setObjectName("horizontalSlider")
        ControlWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ControlWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ControlWindow)
        self.left_button.clicked.connect(self.left_button_clicked)
        self.right_button.clicked.connect(self.right_button_clicked)
        self.horizontalSlider.sliderMoved.connect(self.setPosition)
        self.horizontalSlider.sliderReleased.connect(self.setPosition1)
        self.horizontalSlider.valueChanged.connect(self.updateLCD)
        #self.printit()
        threading.Timer(0.1, self.printit).start()
        for TabName in tabdata:
            TabName = str(TabName)
            print(" TabName", TabName)
            self.TabName = QtWidgets.QWidget()
            self.TabName.setObjectName(TabName)
            self.tabWidget.addTab(self.TabName, TabName)
            try:
                t=TabName.replace(" ","_")
                print(t)
                ListName = t+ "listwidget"
            except:
                ListName = TabName + "listwidget"
                pass
            #ListName = TabName + "listwidget"
            print("List name "+ListName)
            self.ListName = QtWidgets.QListWidget(self.TabName)
            self.ListName.setGeometry(QtCore.QRect(0, 0, 1024, 351))
            self.ListName.setUniformItemSizes(True)
            self.ListName.setFlow(QtWidgets.QListView.TopToBottom)
            self.ListName.setSpacing(50)
            self.ListName.setIconSize(QtCore.QSize(180, 180))
            self.ListName.setWordWrap(True)
            self.ListName.setStyleSheet( "QListView{\n"
                                            "background: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0 #00648E, stop:0.59 #004561, stop:1 #003247);\n"
                                            "border: 0px;\n"
                                            "    font: 16px \"Segoe UI\";\n"
                                            "padding: 0px;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "QScrollBar:horizontal { \n"
                                            "border: 0px; \n"
                                            "background: #044763; \n"
                                            "height: 30px; \n"
                                            "margin: 0px 20px 0px 20px; \n"
                                            "border-radius: 15px;\n"
                                            "}\n"
                                            "QScrollBar::handle:horizontal {\n"
                                            "      background: #FD8800;\n"
                                            "      min-width: 20px;\n"
                                            "    border-radius: 15px;\n"
                                            "}\n"
                                            "\n"
                                            "\n"
                                            "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
                                            "      border: none;\n"
                                            "      background: none;\n"
                                            "}\n"
                                            "\n"
                                            "QListView::item {\n"
                                           "    padding: 5px;\n"
                                           "}\n"
                                            "QListView::item:selected {\n"
                                           "    background: #FD8800;\n"
                                           "}\n"
                                            "QListView::item:hover {\n"
                                           "    background: #FD8800;\n"
                                           "}\n"
                                            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
                                            "    background: none;\n"
                                            "}\n"
                                            "\n"
                                            "QAbstractScrollArea::corner { background: none; border: none; }\n"
                                            "")
            
            self.ListName.setViewMode(QtWidgets.QListView.IconMode)
            print("listname: "+ListName)
            self.ListName.setObjectName(ListName)
            self.add_images_to_TabWIdget(TabName)
            self.ListName.currentTextChanged.connect(self.item_images_clicked)
            self.ListName.setMovement(False)
            

    def getPath(self):
        file = open("path.txt", "r")
        self.directoryPath = file.read()
        self.directoryPath = self.directoryPath.rstrip('\n')
        print(self.directoryPath)

    def left_button_clicked(self):
        currentIndex=self.tabWidget.currentIndex()
        print("current index: "+str(currentIndex))
        currentTab = self.tabWidget.tabText(currentIndex)
        t1=currentTab.replace(" ","_")
        print("current tab: "+currentTab)
        self.listName = self.tabWidget.findChild(QtWidgets.QListWidget, t1 + "listwidget")
        print(self.listName.objectName())
        l=self.listName.objectName()
        cur=self.listName.currentRow()
        if(cur==0):
            print("first item")
        else:
            self.listName.setCurrentRow(cur-1)

    def right_button_clicked(self):
        currentIndex=self.tabWidget.currentIndex()
        print("current index: "+str(currentIndex))
        currentTab = self.tabWidget.tabText(currentIndex)
        t1=currentTab.replace(" ","_")
        print("current tab: "+currentTab)
        self.listName = self.tabWidget.findChild(QtWidgets.QListWidget, t1 + "listwidget")
        print(self.listName.objectName())
        cur=self.listName.currentRow()
        l=len(self.listName)
        print("length = "+str(l))
        if(cur==(l-1)):
            print("last item c={} l={}".format(str(cur),str(l-1)))
        else:
            self.listName.setCurrentRow(cur+1)

    def printit(self):
        global check
        print(check)
        while True:
            if(check==True):
                ms=self.uiV.mediaplayer.get_time()
                self.lcdNumber.display("{}.{}".format(int(ms/60000),int((ms/1000)%60)))
                position = (self.uiV.mediaplayer.get_position()*100)
                print("PositionReceived",position)
                self.horizontalSlider.setValue(position)

    def setPosition(self, position):
        global check
        check=False
        print("setting position: "+str(position/100))
        self.uiV.mediaplayer.set_position(position / 100)
        check= True

    def setPosition1(self):
        global check
        check=False
        print(check)
        print("In set position1 function")
        position=self.horizontalSlider.value()
        p=position/100
        print("in set position1 function: " +str(p))
        self.uiV.mediaplayer.set_position(p)
        check=True
        
    def updateGUI(self):
        pass 

    def updateLCD(self, event):
        print(event)
        self.lcdNumber.display(event)

    def add_images_to_TabWIdget(self, TabName):        
        with open('json_received.json') as f:
            data = json.load(f)
        path = self.directoryPath + "/data/Thumbnails/"
        print(path)
        thumbnail_filename = []
        UUID = []
        content_title = []
        i=0
        j=0
        for entry in self.thumbnail_entries:
            thumbnail_filename.append(entry)
            print(thumbnail_filename[i])
            File_name , ext = thumbnail_filename[i].split(".")
            print("File_name", File_name)
            UUID.append(File_name)
            for t in data:
                if t['CONTENTUUID'] == File_name:
                    print("File_name['CONTENTTITLE']", t['CONTENTTITLE'])
                    if t['CONTENTTITLE'] not in content_title:
                        File_name1 = t['CONTENTTITLE']
                        content_title.append(File_name1)
                        print("content_title", File_name1)
                        print(content_title[j])

            print("UUID Array Print + ", UUID)
            print("Content Title Array Print + ", content_title[j])
            print("Content Title Array Print + ", content_title[j])
            count = content_title[j].count(' ')
            a = content_title[j].split(None, 1)
            if count > 0:
                content_title[j] = a[0] + "\n" + a[1]
                print("BBBBBBBBB", content_title[j])
            else:
                content_title[j] = a[0]
            item1 = QtWidgets.QListWidgetItem(QIcon(path + thumbnail_filename[i]), content_title[j])
            item2 = QtWidgets.QListWidgetItem(QIcon(path + thumbnail_filename[i]), content_title[j])
            content_title[j] = content_title[j].replace("\n"," ")
            print("TabName 23232", TabName)
            for TabName1 in data:

                if (TabName == TabName1['CATTITLE']) and (content_title[j] == TabName1['CONTENTTITLE']):

                    self.ListName.addItem(item2)
            i += 1
            j += 1

    def item_images_clicked(self, item):
        global curframe
        UUID2 = []
        Title = []
        path1 = self.directoryPath + '/data/Content/'
        actual_filename = []
        for entry in self.data_entries:
            actual_filename.append(entry)
        test = item
        print("test", test)
        test = test.replace("\n"," ")
        print("FFFFFFFFFFFFFFFFf", test)
        with open('json_received.json') as f:
            data = json.load(f)
        for data in data:
            if data['CONTENTTITLE'] == test:
                    print("File_name if image clicked =", data['CONTENTUUID'])
                    Item = data['CONTENTITEM']
                    print("Item1", Item)
                    Item1 = Item.split(".")
                    print("Item1[1]", Item1[1])
                    test0 = data['CONTENTUUID'] + "." + Item1[1]
                    test1 = test0
                    print("test1", test1)
        test1 = test1.split(".")
        a = glob.glob(path1 + test1[0] +".*")
        print("value of A " + str(a))
        print(a[0])
        L = a[0].split(".")
        if (curframe==0):
            self.uiV = Ui_VideoWindow()
            widget = self.uiV # define your widget
            display_monitor = 1 # the number of the monitor you want to display your widget
            monitor = QDesktopWidget().screenGeometry(display_monitor)
            widget.move(monitor.left(), monitor.top())
            widget.showFullScreen()
            self.uiV.videoframe.showFullScreen()
            sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))
            self.uiV.label.setGeometry(QtCore.QRect(0, 0, sizeObject.width() , sizeObject.height()))
            self.uiV.label.hide()
        #self.window = QtWidgets.QMainWindow()
        if L[1] == "mp4":
            if (curframe==0):
                curframe=1
                print("Changing from 0 to 1 from mp4")
            if(curframe==2):
                try:
                    print("Changing image frame to video")
                    #self.uiV.photo_label.hide()
                    self.uiV.label.hide()
                    curframe=1
                except:
                    pass
                #self.uiV = Ui_VideoWindow()

            PATH2 = a[0]
            self.uiV.Path(PATH2)
            self.uiV.mediaplayer.play()
            
        else:
            if(curframe==0):
                try:
                    self.uiV.label.showFullScreen()
                    curframe=2
                    print("image current frame photo set 0 to 2")
                except:
                    pass
            else:
                print("Passing 3")
            if(curframe==1):
                try:
                    self.uiV.label.showFullScreen()
                    self.uiV.mediaplayer.stop()
                    curframe=2
                    print("current frame 2 from 1")
                except:
                    pass
            else:
                print("passing 4")
#             display_monitor = 1 # the number of the monitor you want to display your widget
#             monitor = QDesktopWidget().screenGeometry(display_monitor)
#             widget = self.uiV # define your widget
#             widget.showFullScreen()
#             widget.move(monitor.left(), monitor.top())
            #self.uiV.videoframe.showFullScreen()
            #self.uiV.label.showFullScreen()
            #self.uiV.videoframe.hide()
#             self.uiV.mediaplayer.stop()
            print(self.uiV.size())
            sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
            print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))
            self.uiV.label.setPixmap(QtGui.QPixmap(a[0]).scaled(self.uiV.size(), QtCore.Qt.KeepAspectRatio))
#             self.uiV.label.showFullScreen()
#             self.uiV.mediaplayer.stop()

    def retranslateUi(self, ControlWindow):
        _translate = QtCore.QCoreApplication.translate
        ControlWindow.setWindowTitle(_translate("ControlWindow", "MainWindow"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ControlWindow = QtWidgets.QMainWindow()
    ui = Ui_ControlWindow()
    ui.setupUi(ControlWindow)
    ControlWindow.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
    ControlWindow.showFullScreen()
    sys.exit(app.exec_())
