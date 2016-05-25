# -*- encoding : utf-8 -*-
from naoqi import ALProxy
import time

class NaoBehavior:
    naoip = ""
    bhname = ""
    def __init__(self,naoipaddress,behaviorName):
        self.naoip = naoipaddress
        self.bhname = behaviorName
        self.nNB = ALProxy("ALBehaviorManager", self.naoip, 9559)
        self.nposture = ALProxy("ALRobotPosture", self.naoip, 9559)
    def lanuchAndStopBehavior(self):
        if (self.nNB.isBehaviorInstalled(self.bhname)):
            if (not self.nNB.isBehaviorRunning(self.bhname)):
                self.nNB.post.runBehavior(self.bhname)
                time.sleep(5)
            else:
                print "Behavior is already running"
        else:
            print "Behavior is not found"
            return
        names = self.nNB.getRunningBehaviors()
        print "Running behaviors:"
        self.nposture.goToPosture("Stand", 0.5)
        print names
        if (self.nNB.isBehaviorRunning(self.bhname)):
            self.nNB.stopBehavior(self.bhname)
            time.sleep(1.0)
        else:
            print "Behavior is already stopped."

        names = self.nNB.getRunningBehaviors()
        print "Running behaviors:"
        print names


