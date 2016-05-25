# -*- encoding:utf-8 -*-
from comeon1 import *
from naoqi import ALProxy
class Jiayou():

    IP = ""
    def __init__(self, robotIP):
        self.IP = robotIP

    def run(self):

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.176453, -0.176453, -0.580972, -0.572518, -0.193326])

        names.append("HeadYaw")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.0152981, 0.0260359, -0.681138, -0.722556, -0.0123138])

        names.append("LAnklePitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.0827939, 0.337438, -0.314512, -0.520068, 0.0919981])

        names.append("LAnkleRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.138018, -0.05058, -0.101202, -0.0183661, -0.12728])

        names.append("LElbowRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.440216, -1.54462, -0.647306, -1.50021, -0.41107])

        names.append("LElbowYaw")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-1.16742, -1.15361, -0.605972, -0.395814, -1.17048])

        names.append("LHand")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.2908, 0.268, 0.2776, 0.2776, 0.2884])

        names.append("LHipPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.128898, -0.0843279, -0.223922, -0.400332, 0.131966])

        names.append("LHipRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.10282, -0.0168321, -0.0858622, -0.0843279, 0.090548])

        names.append("LHipYawPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.170232, -0.404934, -0.493906, -0.550664, -0.164096])

        names.append("LKneePitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.0828778, -0.0828778, 0.714802, 1.07989, -0.092082])

        names.append("LShoulderPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([1.43885, 0.182504, 0.053648, 0.875872, 1.45266])

        names.append("LShoulderRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.0858622, -0.306841, -0.30991, 0.00149202, 0.139552])

        names.append("LWristYaw")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.0536479, -1.01708, -1.02322, -0.903568, 0.07359])

        names.append("RAnklePitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.0859461, 0.388144, 0.520068, 0.53234, 0.096684])

        names.append("RAnkleRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.138102, 0.11049, 0.265424, 0.270026, 0.128898])

        names.append("RElbowRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.443368, 1.53558, 0.257754, 0.20253, 0.400416])

        names.append("RElbowYaw")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([1.15659, 0.88661, 1.04154, 1.03541, 1.18114])

        names.append("RHand")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.3132, 0.392, 0.254, 0.2724, 0.2952])

        names.append("RHipPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.139552, -0.170316, -0.397348, -0.37894, 0.138018])

        names.append("RHipRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.101202, -0.11194, -0.331302, -0.384992, -0.0950661])

        names.append("RHipYawPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.170232, -0.404934, -0.493906, -0.550664, -0.164096])

        names.append("RKneePitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.0904641, -0.0904641, -0.0889301, -0.0923279, -0.0923279])

        names.append("RShoulderPitch")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([1.42973, 4.19617e-05, -0.51845, -1.27164, 1.44967])

        names.append("RShoulderRoll")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([-0.11049, 0.0628521, -0.642788, -1.04623, -0.162646])

        names.append("RWristYaw")
        times.append([0.84, 1.72, 3.04, 3.52, 5.16])
        keys.append([0.156426, 1.75639, 0.374254, -0.498592, 0.0873961])


        motion = ALProxy("ALMotion", self.IP, 9559)
        say = shuo(self.IP)
        say.run()
        motion.angleInterpolation(names, keys, times, True)


