# -*- coding: utf-8 -*-
import sys
import subprocess
reload(sys)
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from controlls.ConnectNao import *
from mythreads.NaoMovement import *
from LoadBehavior import *
from naoqi import ALProxy
from controlls.MusicPlay import *
import sys
import os
import win32api
from controlls.DanceAlmaters import *
from controlls.face import *
from controlls.comeon import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class LyunNaoTest(QMainWindow):
    NAOIPAddress = ""
    def __init__(self, parent=None):
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
        self.ConnectToNaoAction=QAction(QIcon("F:\NaoTest\NaoSource\mythreads\communicate.png"), self.tr("连接设置"), self)
        self.ConnectToNaoAction.setShortcut("Ctrl+K")
        self.ConnectToNaoAction.setStatusTip(self.tr("连接到NAO机器人"))
        self.connect(self.ConnectToNaoAction, SIGNAL("triggered()"), self.slotConnectToNao)

        self.ControllNaoAction=QAction(QIcon("F:\NaoTest\NaoSource\mythreads\NAOIcon.png"), self.tr("启动控制"), self)
        self.ControllNaoAction.setShortcut("Ctrl+L")
        self.ControllNaoAction.setStatusTip(self.tr("启动对NAO机器人的控制"))
        self.connect(self.ControllNaoAction, SIGNAL("triggered()"), self.slotControllNao)

        self.aboutAction=QAction(self.tr("关于"), self)
        self.connect(self.aboutAction, SIGNAL("triggered()"), self.slotAbout)

        self.connect(self.text, SIGNAL("returnPressed()"), self.slotSpeakControll)

        self.StartVideoWindowAction=QAction(QIcon("F:\NaoTest\NaoSource\controlls\monitor.png"), self.tr("启动监控"), self)
        self.StartVideoWindowAction.setShortcut("Ctrl+M")
        self.StartVideoWindowAction.setStatusTip(self.tr("启动NAO的视频监控"))
        self.connect(self.StartVideoWindowAction, SIGNAL("triggered()"), self.slotStartMonitor)

        self.SmileAction=QAction(QIcon("F:\NaoTest\NaoSource\controlls\smile.png"), self.tr("大笑"), self)
        self.connect(self.SmileAction, SIGNAL("triggered()"), self.slotSmile)

        self.AngryAction = QAction(QIcon("F:\NaoTest\NaoSource\controlls\Angrynew.png"), self.tr("发怒"), self)
        self.connect(self.AngryAction, SIGNAL("triggered()"), self.slotAngry)

        self.DisapointAction = QAction(QIcon("F:\NaoTest\NaoSource\controlls\Disapoint.png"), self.tr("沮丧"), self)
        self.connect(self.DisapointAction, SIGNAL("triggered()"), self.slotDisapoint)

        self.SupriseAction = QAction(QIcon("F:\NaoTest\NaoSource\controlls\Suprise.png"), self.tr("沮丧"), self)
        self.connect(self.SupriseAction, SIGNAL("triggered()"), self.slotSuprise)

        self.SingAction = QAction(QIcon("F:\NaoTest\NaoSource\mythreads\gequ.png"), self.tr("校歌"), self)
        self.connect(self.SingAction, SIGNAL("triggered()"), self.slotSingSong)

        self.Virus = QAction(QIcon("F:\NaoTest\NaoSource\controlls\Viurs.png"), self.tr("病毒"), self)
        self.connect(self.Virus, SIGNAL("triggered()"), self.slotVirus)

        self.Comeon = QAction(QIcon("F:\NaoTest\NaoSource\controlls\comeon1.png"), self.tr("加油"), self)
        self.connect(self.Comeon, SIGNAL("triggered()"),self.slotComeon)

#        self.TaijiAction = QAction(QIcon("F:\NaoTest\NaoSource\controlls\TaiJi.png"), self.tr("校歌"), self)
#        self.connect(self.TaijiAction, SIGNAL("triggered()"), self.slotTaiJi)

    def createMenus(self):
        setMenu=self.menuBar().addMenu(self.tr("设置"))
        setMenu.addAction(self.ConnectToNaoAction)
        setMenu.addAction(self.ControllNaoAction)
        setMenu.addAction(self.StartVideoWindowAction)
        aboutMenu=self.menuBar().addMenu(self.tr("帮助"))
        aboutMenu.addAction(self.aboutAction)

    def createToolBars(self):
        setToolBar=self.addToolBar("Set")
        setToolBar.addAction(self.ConnectToNaoAction)
        setToolBar.addAction(self.ControllNaoAction)
        setToolBar.addAction(self.StartVideoWindowAction)
        setToolBar.addAction(self.SmileAction)
        setToolBar.addAction(self.AngryAction)
        setToolBar.addAction(self.DisapointAction)
        setToolBar.addAction(self.SupriseAction)
        setToolBar.addAction(self.SingAction)
        setToolBar.addAction(self.Virus)
        setToolBar.addAction(self.Comeon)

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
        nNaoMovement=NaoMovement(self.NAOIPAddress)
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
        subprocess.Popen("D:\choregraphe-suite-2.1.4.13-win32-vs2010\bin\monitor-bin.exe")
#        win32api.ShellExecute(0, "open", "D:\choregraphe-suite-2.1.4.13-win32-vs2010\bin\monitor-bin.exe", "", "", 1)
#        os.system('D:\choregraphe-suite-2.1.4.13-win32-vs2010\bin\monitor-bin.exe')
#        os.popen("D:\Program Files (x86)\Dict\YoudaoDict.exe")

    def slotSmile(self):
        self.nNaoBehavior = NaoBehavior(self.NAOIPAddress, "Stand/Emotions/Positive/Laugh_1")
        self.nNaoBehavior.lanuchAndStopBehavior()

    def slotAngry(self):
        self.nNaoBehavior = NaoBehavior(self.NAOIPAddress, "Stand/Emotions/Negative/Angry_2")
        self.nNaoBehavior.lanuchAndStopBehavior()

    def slotDisapoint(self):
        self.nNaoBehavior = NaoBehavior(self.NAOIPAddress, "Stand/Emotions/Negative/Exhausted_2")
        self.nNaoBehavior.lanuchAndStopBehavior()

    def slotSuprise(self):
        self.nNaoBehavior = NaoBehavior(self.NAOIPAddress, "Stand/Emotions/Negative/Surprise_2")
        self.nNaoBehavior.lanuchAndStopBehavior()

    def slotVirus(self):
#        self.nNaoBehavior = NaoBehavior(self.NAOIPAddress, "virus-c811b9/virus/behavior")
 #       self.nNaoBehavior.lanuchAndStopBehavior()
        Virus = virus(self.NAOIPAddress)
        Virus.run()
    def slotComeon(self):
        Comeon = Jiayou(self.NAOIPAddress)
        Comeon.run()


    def slotSingSong(self):
        print "Sing this Song"
        nDance = DanceAlmaters(self.NAOIPAddress)
        nDance.StartDance()

#    def slotTaiJi(self):
#        self.nNaoBehavior = NaoBehavior(self.NAOIPAddress, "TJ1")
#        self.nNaoBehavior.lanuchAndStopBehavior()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LyunNaoTest()
    main.show()
    app.exec_()