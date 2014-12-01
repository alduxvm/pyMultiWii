#!/usr/bin/env python

"""multiwii.py: Handles Multiwii Serial Protocol."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"


import serial, time, struct


class MultiWii:

    """Multiwii Serial Protocol message ID"""
    """ notice: just attitude, rc channels and raw imu are implemented at the moment """
    IDENT = 100
    STATUS = 101
    RAW_IMU = 102
    SERVO = 103
    MOTOR = 104
    RC = 105
    RAW_GPS = 106
    COMP_GPS = 107
    ATTITUDE = 108
    ALTITUDE = 109
    ANALOG = 110
    RC_TUNING = 111
    PID = 112
    BOX = 113
    MISC = 114
    MOTOR_PINS = 115
    BOXNAMES = 116
    PIDNAMES = 117
    WP = 118
    BOXIDS = 119
    RC_RAW_IMU = 121
    SET_RAW_RC = 200
    SET_RAW_GPS = 201
    SET_PID = 202
    SET_BOX = 203
    SET_RC_TUNING = 204
    ACC_CALIBRATION = 205
    MAG_CALIBRATION = 206
    SET_MISC = 207
    RESET_CONF = 208
    SET_WP = 209
    SWITCH_RC_SERIAL = 210
    IS_SERIAL = 211
    DEBUG = 254

    """Global variables of data"""
    rcChannels = {'roll':0,'pitch':0,'yaw':0,'throttle':0,'elapsed':0,'timestamp':0}
    rawIMU = {'ax':0,'ay':0,'az':0,'gx':0,'gy':0,'gz':0,'elapsed':0,'timestamp':0}
    attitude = {'angx':0,'angy':0,'heading':0,'elapsed':0,'timestamp':0}
    temp = ();
    elapsed = 0
    PRINT = 1

    """Serial port initialization"""
    def __init__(self, serPort):
        self.ser = serial.Serial()
        self.ser.port = serPort
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 0
        self.ser.xonxoff = False
        self.ser.rtscts = False
        self.ser.dsrdtr = False
        self.ser.writeTimeout = 2
        """Time to wait until the board becames operational"""
        wakeup = 12
        try:
            self.ser.open()
            if MultiWii.PRINT:
                print "Waking up multicopter on "+self.ser.port+"..."
            for i in range(1,wakeup):
                if MultiWii.PRINT:
                    print wakeup-i
                    time.sleep(1)
                else:
                    time.sleep(1)
        except Exception, error:
            print "\n\nError opening "+self.ser.port+" port.\n\n"
            quit()

    """Function for sending a command to the board"""
    def sendCMD(self, data_length, code, data):
        checksum = 0
        total_data = ['$', 'M', '<', data_length, code] + data
        for i in struct.pack('<2B%dh' % len(data), *total_data[3:len(total_data)]):
            checksum = checksum ^ ord(i)
        total_data.append(checksum)
        try:
            b = None
            b = self.ser.write(struct.pack('<3c2B%dhB' % len(data), *total_data))
        except Exception, error:
            print "\n\nError is sendCMD."
            print "("+str(error)+")\n\n"
            self.ser.close()
            quit()
        return b

    """Function to receive a data packet from the board"""
    def getData(self, cmd):
        try:
            start = time.time()
            self.sendCMD(0,cmd,[])
            while True:
                header = self.ser.read()
                if header == '$':
                    header = header+self.ser.read(2)
                    break
            datalength = struct.unpack('<b', self.ser.read())[0]
            code = struct.unpack('<b', self.ser.read())
            data = self.ser.read(datalength)
            temp = struct.unpack('<'+'h'*(datalength/2),data)
            elapsed = time.time() - start
            self.ser.flushInput()
            self.ser.flushOutput()
            if cmd == MultiWii.ATTITUDE:
                MultiWii.attitude['angx']=float(temp[0]/10.0)
                MultiWii.attitude['angy']=float(temp[1]/10.0)
                MultiWii.attitude['heading']=float(temp[2])
                MultiWii.attitude['elapsed']=round(elapsed,3)
                MultiWii.attitude['timestamp']=time.time()
                return MultiWii.attitude
            elif cmd == MultiWii.RC:
                for value in MultiWii.rcChannels:
                    MultiWii.rcChannels[value]=temp[i]
                    i+=1
                MultiWii.rcChannels['elapsed']=round(elapsed,3)
                MultiWii.rcChannels['timestamp']=time.time()
                return MultiWii.rcChannels
            elif cmd == MultiWii.RAW_IMU:
                MultiWii.rawIMU['ax']=float(temp[0])
                MultiWii.rawIMU['ay']=float(temp[1])
                MultiWii.rawIMU['az']=float(temp[2])
                MultiWii.rawIMU['gx']=float(temp[3])
                MultiWii.rawIMU['gy']=float(temp[4])
                MultiWii.rawIMU['gz']=float(temp[5])
                MultiWii.rawIMU['elapsed']=round(elapsed,3)
                MultiWii.rawIMU['timestamp']=time.time()
                return MultiWii.rawIMU
            else:
                return "No return error!"
        except Exception, error:
            print error



