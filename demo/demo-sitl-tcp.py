""" Demo to connect to firmwarm running as SITL over TCP using the MSP """

__author__ = "William Koch"

from pymultiwii import MultiWii
import time
import signal
import sys



def signal_handler(signal, frame):
    print(' Ctrl+C!')
    aircraft.disarm()
    fc.close()
    sys.exit(0)

# NEED TO MATCH THE CHANNEL MAPPING!
# This is using AETR1234
class TCPGroundStation(object):
    DELAY = 5
    MIN_THROTTLE =1000
    ARM = 1800
    DISARM = 1000

    def __init__(self, fc):
        self.fc = fc

    def takeoff(self):
        self.fc.sendCMD(MultiWii.SET_RAW_RC)

    def readRC(self):
        self.fc.getData(MultiWii.RC)
        rc = self.fc.rcChannels
        print "roll={} pitch={} yaw={} throttle={}".format(rc['roll'], rc['pitch'], rc['yaw'], rc['throttle'])
        time.sleep(0.1)

    def readIMU(self):
        self.fc.getData(MultiWii.RAW_IMU)
        imu = self.fc.rawIMU
        print "ax={} ay={} az={} gx={} gy={} gz={}".format(imu['ax'], imu['ay'], imu['az'], imu['gx'], imu['gy'], imu['gz'])

    def liftoff(self):
        timer = 0
        start = time.time()
        while timer < self.DELAY:
            length = 16
            data = [1500, 1500, 1900, 1500, self.ARM, 1000, 1000, 1000]
            self.fc.sendCMD(length, MultiWii.SET_RAW_RC, data)

            time.sleep(0.05)
            timer = timer + (time.time() - start)
            start =  time.time()

    def arm(self):
        timer = 0
        start = time.time()
        while timer < self.DELAY:
            data = [1500, 1500,self.MIN_THROTTLE, 1500, self.ARM, 1000, 1000, 1000 ]
            self.fc.sendCMD(16, MultiWii.SET_RAW_RC,data)
            time.sleep(0.05)
            timer = timer + (time.time() - start)
            start =  time.time()

    def disarm(self):
        timer = 0
        start = time.time()
        while timer < self.DELAY:#0.5:
            data = [1500, 1500, self.MIN_THROTTLE, 1500, self.DISARM, 1000, 1000, 1000 ]
            self.fc.sendCMD(16,MultiWii.SET_RAW_RC,data)
            time.sleep(0.05)
            timer = timer + (time.time() - start)
            start =  time.time()

if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    # Connect to the Betaflight TCP server
    port = "tcp://127.0.0.1:5761"

    fc = MultiWii(port)
    fc.connect()

    aircraft = TCPGroundStation(fc)

    aircraft.readRC()

    print "Disarm..."
    aircraft.disarm()

    aircraft.readRC()

    print "Arming..."
    aircraft.arm()

    print aircraft.readIMU()

    print "Lift off..."
    while True:
        aircraft.liftoff()
        aircraft.readRC()
        aircraft.readIMU()
