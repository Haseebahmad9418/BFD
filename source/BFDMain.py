# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
import requests
import json
import os,sys
from os import path
import urllib
import download
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from subprocess import check_output


from InitialDeviceRegisterSyncCredentialsError import Ui_CredentialsError #Import Files of all GUI's
from register import Ui_register_2
from LaunchVdownload import Ui_Launch
from InitialDeviceRegisterSyncSuccess import Ui_InitialRegSuccess
from RegistedDeviceSyncSuccess import Ui_SyncSuccess
from Main import Ui_Main
from MainControl import Ui_ControlWindow
from RegisteredDeviceSync import Ui_DeviceSync
from InitialDeviceRegisterTransferError import Ui_TransferError
from RegistedDeviceDownloadingcontent import Ui_SyncSuccess1
from RegisteredCopyright import Ui_RegisteredCopyright
from UnregisteredCopyright import Ui_Unregistered
from wifi import Ui_Wifilist
from wifipassword import Ui_Wifi

class Downloading(QtWidgets.QMainWindow, Ui_SyncSuccess1):  #Class to acces Main.py GUI

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_SyncSuccess1, self).__init__()
        self.setupUi(self)



class wifilisting(QtWidgets.QMainWindow, Ui_Wifilist):  #Class to acces Main.py GUI
    refresh = pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Wifilist, self).__init__()
        self.setupUi(self)
        self.PushButton_2.clicked.connect(lambda: self.refreshlist())
        self.refreshlist()
        self.listWidget.clicked.connect(self.clicked)

    def clicked(self,item):
        global selectedssid
        item=self.listWidget.currentItem()
        selectedssid=item.text()
        print(item.text())
        self.refresh.emit()
        pass

    def refreshlist(self):
        try:
            scanoutput = check_output(["iwlist", "wlan0", "scan"])
            ss=scanoutput.decode("utf-8")
            self.listWidget.clear()
            ssid=[]
            for line in ss.split("\n"):
               if "ESSID" in line:
                   ssid = line.split('"')[1]
                   print(ssid)
                   item=QtWidgets.QListWidgetItem(ssid,self.listWidget)
                   item.setTextAlignment(QtCore.Qt.AlignCenter)
                   #self.ssidlist.addItem(item)
        except:
            pass
            
class wifipw(QtWidgets.QMainWindow, Ui_Wifi):  #Class to acces Main.py GUI
    switch_wpdone = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Wifi, self).__init__()
        self.setupUi(self)
        self.PushButton_2.clicked.connect(lambda: self.connectwifi())

    def connectivity(self):
        try:
            urllib.request.urlopen("https://www.google.com/",timeout=2)
            return True
        except:
            pass
            return False
        
    def connectwifi(self):
        self.framestatus.setGeometry(QtCore.QRect(312, 200, 400, 200))
        app.processEvents()
        global selectedssid
        print(selectedssid)
        pw=self.lineEdit.text()
        print(pw)
        wififile=directoryPath+"/source/wifi.txt"
        wfile=os.path.isfile(wififile)
        if(wfile==False):
            file1=open(wififile,'w+')
            file1.write("")
            file1.close()
        file1=open(wififile,'w+')
        data=selectedssid+"; "+pw+"; "
        file1.write(data)
        file1.close()
        config = (
        '\nnetwork={{\n' +
        '\tssid="{}"\n' +
        '\tpsk="{}"\n' + '}}').format(selectedssid, pw)
        with open("/etc/wpa_supplicant/wpa_supplicant.conf") as f:
            if config in f.read():
                print("Already in file\n"+config)
            else:
                with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a+") as wifi:
                    wifi.write(config)
                    wifi.close()
            f.close()
        os.system("wpa_cli -i wlan0 reconfigure")
        time.sleep(20)
        i=self.connectivity()
        if(i==False):
            self.label_2.setText("Wrong Credentials. Removing!")
            app.processEvents()
            print("no coneection")
            fin=open("/etc/wpa_supplicant/wpa_supplicant.conf","rt")
            data = fin.read()
            data = data.replace(config, "")
            fin.close()
            fin=open("/etc/wpa_supplicant/wpa_supplicant.conf","wt")
            fin.write(data)
            fin.close()
            os.system("wpa_cli -i wlan0 reconfigure")
            time.sleep(15)
        self.switch_wpdone.emit()
        pass

class Main(QtWidgets.QMainWindow, Ui_Main):  #Class to acces Main.py GUI
    switch_Launch = QtCore.pyqtSignal()
    switch_Register = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Main, self).__init__()
        self.setupUi(self)
        self.PushButton_2.clicked.connect(lambda: self.pressLaunch())
        self.PushButton.clicked.connect(lambda: self.pressRegister())
        
    def pressLaunch(self):
        print('LaunchSuccess press')
        self.switch_Launch.emit()
        pass
        
    def pressRegister(self):
        print('RegisterSuccess press')
        self.switch_Register.emit()
        pass

class Launch(QtWidgets.QMainWindow, Ui_Launch):  #Class to acces LaunchVDownload.py GUI
    switch_SyncSuccess = QtCore.pyqtSignal()
    switch_ControlWindow = QtCore.pyqtSignal()
    switch_RegisteredCopyright = QtCore.pyqtSignal()
    switch_DeviceSync = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Launch, self).__init__()
        self.setupUi(self)
        self.PushButton_4.clicked.connect(lambda: self.Download())
        self.PushButton_2.clicked.connect(lambda: self.Download())
        self.PushButton.clicked.connect(lambda: self.pressControlWindow())
        self.PushButton_3.clicked.connect(lambda: self.pressControlWindow())
        self.pushButton5.clicked.connect(lambda: self.pressRegisteredCopyright())
        
    def Download(self):
        print('SyncSuccess press')
        self.switch_SyncSuccess.emit()
            
    def pressControlWindow(self):
        print('ControlWindow press')
        self.switch_ControlWindow.emit()
        pass
    
    def pressRegisteredCopyright(self):
        print("RegisteredCopyright press")
        self.switch_RegisteredCopyright.emit()
        pass

class Register(QtWidgets.QMainWindow, Ui_register_2): #Class to access register.py GUI
    switch_Main = QtCore.pyqtSignal()
    switch_UnregisteredCopyright = QtCore.pyqtSignal()
    switch_CredentialsError = QtCore.pyqtSignal()
    switch_InitialRegSuccess = QtCore.pyqtSignal()
    switch_TransferError = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        print ("setup Register")
        super(Ui_register_2, self).__init__()
        self.setupUi(self)        
        self.pushButton.clicked.connect(lambda: self.pressUnregisteredCopyright())
        self.PushButton.clicked.connect(lambda: self.check_password())
        
    def pressUnregisteredCopyright(self):
        print("UnregisteredCopyright press")
        self.switch_UnregisteredCopyright.emit()
        pass
    
    def check_password(self):
        check = 1
        if check == 1:
            try:
                print('Success')
                customer = self.lineEdit.text()
                software = self.lineEdit_2.text()
                requ = ("http://bigfatdisplays.com/bigfatdisplays/?ClientKey="+customer+"&KioskKey="+software)
                
                print(requ)
                json1 = requests.get(requ)
                json2 = json.loads(json1.text)

                if json2 == "No Records Found":
                    print('Wrong Password')
                    self.switch_CredentialsError.emit() 
                
                else:
                    with open("json_received.json", "w+") as f:
                        json.dump(json2, f)
                    f= open("credentials.txt","w+")
                    f.write(customer)
                    f.write("." + software)
                    f.close()
                    self.switch_InitialRegSuccess.emit()
            except:
                self.switch_CredentialsError.emit()

class SyncSuccess(QtWidgets.QMainWindow, Ui_SyncSuccess): #Class to access RegistedDeviceSyncSuccess.py GUI
    switch_Launch = QtCore.pyqtSignal()
    switch_ControlWindow = QtCore.pyqtSignal()
    switch_DeviceSync = QtCore.pyqtSignal()
    switch_RegisteredCopyright = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_SyncSuccess, self).__init__()
        self.setupUi(self)
        self.PushButton_4.clicked.connect(lambda: self.pressControlWindow())
        self.pushButton_2.clicked.connect(lambda: self.pressRegisteredCopyright())
        
    def pressControlWindow(self):
        print('ControlWindow press')
        self.switch_ControlWindow.emit()
        pass
    
    def pressRegisteredCopyright(self):
        print("RegisteredCopyright press")
        self.switch_RegisteredCopyright.emit()
        pass   
        
class DeviceSync(QtWidgets.QMainWindow, Ui_DeviceSync): #Class to access RegistedDeviceSyncSuccess.py GUI
    switch_SyncSuccess = QtCore.pyqtSignal()
    switch_Launch = QtCore.pyqtSignal()
    switch_RegisteredCopyright = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_DeviceSync, self).__init__()
        self.setupUi(self)
        self.PushButton_2.clicked.connect(lambda: self.pressSyncSuccess())
        self.PushButton_4.clicked.connect(lambda: self.pressSyncSuccess())
        self.pushButton.clicked.connect(lambda: self.pressRegisteredCopyright())
        
    def pressSyncSuccess(self):
        print("SyncSuccess press")
        self.switch_SyncSuccess.emit()
        pass
    
    def pressRegisteredCopyright(self):
        print("RegisteredCopyright press")
        self.switch_RegisteredCopyright.emit()
        pass    
        
class UnregisteredCopyright(QtWidgets.QMainWindow, Ui_Unregistered): #Class to access UnregisteredCopyright.py GUI
    switch_Register = QtCore.pyqtSignal()
    switch_DeviceSync = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_Unregistered, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.pressRegister())
        
    def pressRegister(self):
        print('RegisterSuccess press')
        self.switch_Register.emit()
        pass
        
class RegisteredCopyright(QtWidgets.QMainWindow, Ui_RegisteredCopyright): #Class to access RegisteredCopyright.py GUI
    switch_SyncSuccess = QtCore.pyqtSignal()
    switch_Launch = QtCore.pyqtSignal()
    switch_DeviceSync = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_RegisteredCopyright, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.pressLaunch())
        
    def pressLaunch(self):
        print('LaunchSuccess press')
        self.switch_Launch.emit()
        pass
        
class CredentialsError(QtWidgets.QMainWindow, Ui_CredentialsError):  #Class to access CredentialsError.py GUI
    switch_Register = QtCore.pyqtSignal()
    switch_UnregisteredCopyright = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_CredentialsError, self).__init__()
        self.setupUi(self)
        self.PushButton_4.clicked.connect(lambda: self.pressRegister())
        self.PushButton_2.clicked.connect(lambda: self.pressRegister())
        self.pushButton.clicked.connect(lambda: self.pressUnregisteredCopyright())
        
    def pressRegister(self):
        print('RegisterSuccess press')
        self.switch_Register.emit()
        pass
    
    def pressUnregisteredCopyright(self):
        print("UnregisteredCopyright press")
        self.switch_UnregisteredCopyright.emit()
        pass
        
class InitialRegSuccess(QtWidgets.QMainWindow, Ui_InitialRegSuccess): #Class to access InitialDeviceRegisterSyncSuccess.py GUI
    switch_ControlWindow = QtCore.pyqtSignal()
    switch_Register = QtCore.pyqtSignal()
    switch_UnregisteredCopyright = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_InitialRegSuccess, self).__init__()
        self.setupUi(self)
        self.PushButton_4.clicked.connect(lambda: self.pressControlWindow())
        self.pushButton_2.clicked.connect(lambda: self.pressUnregisteredCopyright())
    
    def pressControlWindow(self):
        print('ControlWindow press')
        self.switch_ControlWindow.emit()
        pass
        
    def pressUnregisteredCopyright(self):
        print("UnregisteredCopyright press")
        self.switch_UnregisteredCopyright.emit()
        pass
        
class TransferError(QtWidgets.QMainWindow, Ui_TransferError): #Class to access InitialDeviceRegisterSyncSuccess.py GUI
    switch_Register = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_TransferError, self).__init__()
        self.setupUi(self)
        self.PushButton_4.clicked.connect(lambda: self.pressRegister())
        self.PushButton_2.clicked.connect(lambda: self.pressRegister())
    
    def pressRegister(self):
        self.switch_Register.emit()
        pass

class ControlWindow(QtWidgets.QMainWindow, Ui_ControlWindow): #Class to access InitialDeviceRegisterSyncSuccess.py GUI
    switch_SyncSuccess = QtCore.pyqtSignal()
    switch_Launch = QtCore.pyqtSignal()
    switch_InitialRegSuccess = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        super(Ui_ControlWindow, self).__init__()
        self.setupUi(self)    

class Controller:   # Controller class which controlls all the functions
    def __init__(self):
        print("In controller class")        
        self._Downloading=Downloading()
        self._SyncSuccess = SyncSuccess()
        self._Launch = Launch()
        self._Main = Main()
        self._Register = Register()
        self._UnregisteredCopyright = UnregisteredCopyright()
        self._RegisteredCopyright = RegisteredCopyright()
        self._CredentialsError = CredentialsError()
        self._InitialRegSuccess = InitialRegSuccess()
        self._TransferError = TransferError()
        self._DeviceSync = DeviceSync()
        self._ControlWindow = ControlWindow()
        self._wifilisting=wifilisting()
        self._wifipw=wifipw()
        pass
    
    def show_wifilisting_page(self):
        self._wifilisting.close()
        self._wifilisting=wifilisting()
        self._wifilisting.refresh.connect(self.show_wifipw_page)
        self._wifilisting.showFullScreen()
        self._wifipw.close()
        
    def show_wifipw_page(self):
        self._wifipw.close()
        self._wifipw=wifipw()
        self._wifipw.switch_wpdone.connect(self.check)
        self._wifipw.showFullScreen()
        self._wifilisting.close()
        
    def check(self):
        e = path.exists(directoryPath+"/source/credentials.txt")
        print(e)
        internet=self.conectivity()
        if internet== False:
            self.show_wifilisting_page()
        elif e == True:
            self.show_Launch_page()
        elif e == False:
            self.show_Register_page()

    def show_download1_page(self):
        self._Downloading.close()
        self._Downloading= Downloading()
        self._Downloading.showFullScreen()
        self._Launch.close()
        loop=QtCore.QEventLoop()
        QTimer.singleShot(2000,loop.quit)
        loop.exec_()
        download.download()
        self.show_SyncSuccess_page()
        
    def show_download_page(self):
        self._Downloading.close()
        self._Downloading= Downloading()
        self._Downloading.showFullScreen()
        loop=QtCore.QEventLoop()
        QTimer.singleShot(2000,loop.quit)
        loop.exec_()
        self._Register.close()
        download.download()
        self.show_InitialRegSuccess_page()
        
    def show_Main_page(self):
        self._Main.close()
        self._Main = Main()
        self._Main.switch_Launch.connect(self.show_Launch_page)
        self._Main.switch_Register.connect(self.show_Register_page)
        self._Main.close()
        self._Main.showFullScreen()
        pass
    
    def show_Launch_page(self):
        self._Launch.close()
        self._Main.close()
        self._RegisteredCopyright.close()
        self._Launch = Launch()
        self._Launch.switch_SyncSuccess.connect(self.show_download1_page)
        self._Launch.switch_ControlWindow.connect(self.show_ControlWindow_page)
        self._Launch.switch_RegisteredCopyright.connect(self.show_RegisteredCopyright_page)
        self._Launch.showFullScreen()
        self._wifipw.close()
        
    def show_Register_page(self):
        self._CredentialsError.close()
        self._Register.close()
        self._TransferError.close()
        self._Main.close()
        self._Register = Register()
        self._Register.switch_UnregisteredCopyright.connect(self.show_UnregisteredCopyright_page)
        self._Register.switch_CredentialsError.connect(self.show_CredentialsError_page)
        self._Register.switch_InitialRegSuccess.connect(self.show_download_page)
        self._Register.switch_TransferError.connect(self.show_TransferError_page)
        self._UnregisteredCopyright.close()
        self._Register.showFullScreen()
        self._wifipw.close()
        pass
        
    def show_InitialRegSuccess_page(self):
        self._InitialRegSuccess.close()
        self._InitialRegSuccess = InitialRegSuccess()
        self._InitialRegSuccess.switch_Register.connect(self.show_Register_page)
        self._InitialRegSuccess.switch_ControlWindow.connect(self.show_ControlWindow_page)
        self._InitialRegSuccess.switch_UnregisteredCopyright.connect(self.show_UnregisteredCopyright_page)
        self._Register.close()
        self._Downloading.close()
        self._InitialRegSuccess.showFullScreen()
        pass
    
    def show_CredentialsError_page(self):
        self._CredentialsError.close()
        self._Register.close()
        self._CredentialsError = CredentialsError()
        self._CredentialsError.switch_Register.connect(self.show_Register_page)
        self._CredentialsError.switch_UnregisteredCopyright.connect(self.show_UnregisteredCopyright_page)
        self._Register.close()
        self._UnregisteredCopyright.close()
        self._CredentialsError.showFullScreen()
        pass
    
    def show_UnregisteredCopyright_page(self):
        self._UnregisteredCopyright.close()
        self._InitialRegSuccess.close()
        self._CredentialsError.close()
        self._UnregisteredCopyright = UnregisteredCopyright()
        self._UnregisteredCopyright.switch_Register.connect(self.show_Register_page)
        self._Register.close()
        self._UnregisteredCopyright.showFullScreen()
        pass
    
    def show_RegisteredCopyright_page(self):
        self._RegisteredCopyright.close()
        self._SyncSuccess.close()
        self._DeviceSync.close()
        self._RegisteredCopyright = RegisteredCopyright()
        self._RegisteredCopyright.switch_Launch.connect(self.show_Launch_page)
        self._RegisteredCopyright.switch_DeviceSync.connect(self.show_DeviceSync_page)
        self._RegisteredCopyright.switch_SyncSuccess.connect(self.show_SyncSuccess_page)
        self._Launch.close()
        self._RegisteredCopyright.showFullScreen()
        pass
    
    def show_SyncSuccess_page(self):
        self._SyncSuccess.close()
        self._Launch.close()
        self._DeviceSync.close()
        self._SyncSuccess = SyncSuccess()
        self._SyncSuccess.switch_ControlWindow.connect(self.show_ControlWindow_page)
        self._SyncSuccess.switch_DeviceSync.connect(self.show_DeviceSync_page)
        self._SyncSuccess.switch_RegisteredCopyright.connect(self.show_RegisteredCopyright_page)
        self._DeviceSync.close()
        self._Downloading.close()
        self._SyncSuccess.showFullScreen()
        pass
    
    def show_DeviceSync_page(self):
        self._DeviceSync.close()
        self._DeviceSync = DeviceSync()
        self._DeviceSync.switch_Launch.connect(self.show_Launch_page)
        self._DeviceSync.switch_SyncSuccess.connect(self.show_SyncSuccess_page)
        self._DeviceSync.switch_RegisteredCopyright.connect(self.show_RegisteredCopyright_page)
        self._Launch.close()
        self._DeviceSync.showFullScreen()
        pass
    
    def show_TransferError_page(self):
        self._TransferError.close()
        self._TransferError = TransferError()
        self._TransferError.switch_Register.connect(self.show_Register_page)
        self._Register.close()
        self._TransferError.showFullScreen()
        pass
    
    def show_ControlWindow_page(self):
        self._ControlWindow.close()
        self._SyncSuccess.close()
        self._ControlWindow = ControlWindow()
        self._ControlWindow.switch_Launch.connect(self.show_Launch_page)
        self._Launch.close()
        self._SyncSuccess.close()
        self._InitialRegSuccess.close()
        self._ControlWindow.showFullScreen()
        pass
    
    def conectivity(self):
        try:
            urllib.request.urlopen("https://www.google.com/",timeout=2)
            return True
        except:
            return False
            
import source_rc
if __name__ == "__main__":
    print("Main")
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    print("Calling splash")
    file = open("path.txt", "r")
    directoryPath = file.read()
    file.close()
    e = path.exists(directoryPath+"/source/credentials.txt")
    print(e)
    internet=controller.conectivity()
    if internet==False:
        controller.show_wifilisting_page()
    elif e == True:
        controller.show_Launch_page()
    elif e == False:   
        controller.show_Register_page()
    sys.exit(app.exec_())