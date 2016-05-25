# -*- encoding:UTF-8 -*-
from mythreads.NaoMovement import *
from mythreads.NaoSay import *
from LyunNaoTest import *
from NaoViews import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    nMainViews=NaoViews()
    nMainViews.show()
    app.exec_()


