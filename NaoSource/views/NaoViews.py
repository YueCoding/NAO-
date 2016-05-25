# -*- coding: utf-8 -*-
import sys
import subprocess
reload(sys)
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from controlls.ConnectNao import *
from mythreads.NaoMovement import *
from naoqi import ALProxy
import sys

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class LyunNaoTest(QMainWindow):
    NAOIPAddress = ""
    def __init__(self,parent=None):
        super(LyunNaoTest, self).__init__(parent)
        self.setWindowTitle(self.tr("龙岩学院_龙之舞"))
        self.resize(800, 600)
        self.text = QLineEdit()
        self.setCentralWidget(self.text)
        self.text.setFocus()
        self.center()

        self.createActions()
        self.createMenus()
        self.createToolBars()


    def createActions(self):
        self.ConnectToNaoAction = QAction(QIcon("F:\NaoTest\NaoSource\mythreads\communicate.png"), self.tr("连接设置"), self)
        self.ConnectToNaoAction.setShortcut("Ctrl+K")
        self.ConnectToNaoAction.setStatusTip(self.tr("连接到NAO机器人"))
        self.connect(self.ConnectToNaoAction, SIGNAL("triggered()"), self.slotConnectToNao)

        self.ControllNaoAction = QAction(QIcon("/home/winfield.he/PycharmProjects/NaoTest/NaoSource/mythreads/NAOIcon.png"), self.tr("启动控制"), self)
        self.ControllNaoAction.setShortcut("Ctrl+L")
        self.ControllNaoAction.setStatusTip(self.tr("启动对NAO机器人的控制"))
        self.connect(self.ControllNaoAction, SIGNAL("triggered()"), self.slotControllNao)

        self.aboutAction = QAction(self.tr("关于"),self)
        self.connect(self.aboutAction, SIGNAL("triggered()"), self.slotAbout)

        self.connect(self.text, SIGNAL("returnPressed()"), self.slotSpeakControll)

        self.StartVideoWindowAction = QAction(QIcon("/home/winfield.he/PycharmProjects/NaoTest/NaoSource/controlls/monitor.png"), self.tr("启动监控"), self)
        self.StartVideoWindowAction.setShortcut("Ctrl+M")
        self.StartVideoWindowAction.setStatusTip(self.tr("启动NAO的视频监控"))
        self.connect(self.StartVideoWindowAction, SIGNAL("triggered()"), self.slotStartMonitor)
    def createMenus(self):
        setMenu = self.menuBar().addMenu(self.tr("设置"))
        setMenu.addAction(self.ConnectToNaoAction)
        setMenu.addAction(self.ControllNaoAction)
        setMenu.addAction(self.StartVideoWindowAction)

        aboutMenu = self.menuBar().addMenu(self.tr("帮助"))
        aboutMenu.addAction(self.aboutAction)

    def createToolBars(self):
        setToolBar = self.addToolBar("Set")
        setToolBar.addAction(self.ConnectToNaoAction)
        setToolBar.addAction(self.ControllNaoAction)
        setToolBar.addAction(self.StartVideoWindowAction)
    def slotAbout(self):
        QMessageBox.about(self, self.tr("龙之舞作品"), self.tr("龙岩学院NAO机器人应用测试版本V1.0"))
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
    def slotConnectToNao(self):
        text, ok = QInputDialog.getText(self, self.tr("NAO的IP地址设置"), self.tr("请输入待连接NAO的IP地址"))
        if ok:
            nConnectNao = ConnectNao()
            nConnectNao.setNaoIP(str(text))
            self.NAOIPAddress = nConnectNao.getNaoIP()
            print self.NAOIPAddress
            self.NaoSayInit()
    def slotControllNao(self):
        nNaoMovement = NaoMovement(self.NAOIPAddress)
        nNaoMovement.start()
    def slotSpeakControll(self):
        self.speakcontext = self.text.text()
        print unicode(self.text.text())
        self.text.clear()
        self.naosay.say(str(self.speakcontext), self.configuration)
    def NaoSayInit(self):
        self.naosay = ALProxy("ALAnimatedSpeech", self.NAOIPAddress, 9559)
        self.naosayset = ALProxy("ALTextToSpeech", self.NAOIPAddress, 9559)
        self.configuration = {"bodyLanguageMode": "contextual"}
        self.naosayset.setLanguage("Chinese")
        sys.setdefaultencoding("utf-8")
    def slotStartMonitor(self):
        print ("Monitor Ok")
        subprocess.Popen('/opt/Aldebaran Robotics/Choregraphe Suite 2.1/bin/monitor-bin')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LyunNaoTest()
    main.show()
    app.exec_()

