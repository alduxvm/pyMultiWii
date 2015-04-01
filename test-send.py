#!/usr/bin/env python

"""test-send.py: Test script to send RC commands to a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pyMultiwii import MultiWii

if __name__ == "__main__":

    serialPort = "/dev/tty.usbserial-A801WZA1"
    #serialPort = "/dev/tty.SLAB_USBtoUART"
    board = MultiWii(serialPort)
    try:
        while True:
        	#example of 8 RC channels to be send
            data = [1500,1500,1500,1500,1000,1000,1000,1000]
            board.sendCMD(16,MultiWii.SET_RAW_RC,data)
            #After sending, we ask for attitude and rc commands to see if the commands are being applied
            board.getData2cmd(MultiWii.ATTITUDE)
            print board.message
    except Exception,error:
        print "Error on Main: "+str(error)