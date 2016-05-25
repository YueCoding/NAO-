# -*- encoding:utf-8 -*-
from controlls.Shuo import *
from naoqi import ALProxy



class virus():

    IP = ""
    def __init__(self, robotIP):

        self.IP = robotIP

    def run(self):

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([1, 2.56])
        keys.append([-0.182588, -0.449518])

        names.append("HeadYaw")
        times.append([1, 2.56])
        keys.append([0, 1.0216])

        names.append("LAnklePitch")
        times.append([1, 2.56])
        keys.append([0.0981341, 0.0873961])

        names.append("LAnkleRoll")
        times.append([1, 2.56])
        keys.append([-0.122678, -0.122678])

        names.append("LElbowRoll")
        times.append([1, 2.56])
        keys.append([-0.4034, -0.446352])

        names.append("LElbowYaw")
        times.append([1, 2.56])
        keys.append([-1.2165, -1.32082])

        names.append("LHand")
        times.append([1, 2.56])
        keys.append([0.2896, 0.2896])

        names.append("LHipPitch")
        times.append([1, 2.56])
        keys.append([0.127364, 0.127364])

        names.append("LHipRoll")
        times.append([1, 2.56])
        keys.append([0.0951499, 0.0951499])

        names.append("LHipYawPitch")
        times.append([1, 2.56])
        keys.append([-0.168698, -0.168698])

        names.append("LKneePitch")
        times.append([1, 2.56])
        keys.append([-0.0923279, -0.0923279])

        names.append("LShoulderPitch")
        times.append([1, 2.56])
        keys.append([1.4818, -0.320648])

        names.append("LShoulderRoll")
        times.append([1, 2.56])
        keys.append([0.168698, 0.27301])

        names.append("LWristYaw")
        times.append([1, 2.56])
        keys.append([0.0797259, -0.39428])

        names.append("RAnklePitch")
        times.append([1, 2.56])
        keys.append([0.0813439, 0.092082])

        names.append("RAnkleRoll")
        times.append([1, 2.56])
        keys.append([0.127364, 0.127364])

        names.append("RElbowRoll")
        times.append([1, 2.56])
        keys.append([0.415757, 1.54018])

        names.append("RElbowYaw")
        times.append([1, 2.56])
        keys.append([1.21028, 0.697927])

        names.append("RHand")
        times.append([1, 2.56])
        keys.append([0.2908, 0.2908])

        names.append("RHipPitch")
        times.append([1, 2.56])
        keys.append([0.128814, 0.128814])

        names.append("RHipRoll")
        times.append([1, 2.56])
        keys.append([-0.093532, -0.093532])

        names.append("RHipYawPitch")
        times.append([1, 2.56])
        keys.append([-0.168698, -0.168698])

        names.append("RKneePitch")
        times.append([1, 2.56])
        keys.append([-0.0827939, -0.0827939])

        names.append("RShoulderPitch")
        times.append([1, 2.56])
        keys.append([1.45888, 0.773177])

        names.append("RShoulderRoll")
        times.append([1, 2.56])
        keys.append([-0.170316, 0.233125])

        names.append("RWristYaw")
        times.append([1, 2.56])
        keys.append([0.0904641, 0.444818])

        motion = ALProxy("ALMotion", self.IP, 9559)
        tosay = shuo(self.IP)
        motion.angleInterpolation(names, keys, times, True)
        tosay.run()
        time.sleep(0.8)
        posture = ALProxy("ALRobotPosture", self.IP, 9559)
        posture.goToPosture("Stand", 0.5)
