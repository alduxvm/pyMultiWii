#!/usr/bin/env python

"""test-attitude.py: Main module to test communication with a MultiWii Board by asking attitude."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pyMultiwii import MultiWii

if __name__ == "__main__":

    #board = MultiWii("/dev/ttyUSB0")
    board = MultiWii("/dev/tty.usbserial-A801WZA1")
    try:
        while True:
            board.getData(MultiWii.ATTITUDE)
            print board.attitude
    except Exception,error:
        print "Error on Main: "+str(error)