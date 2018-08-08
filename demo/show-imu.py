#!/usr/bin/env python

"""show-attitude.py: Script to ask the MultiWii Board attitude and print it."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2017 Altax.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pymultiwii import MultiWii
from sys import stdout

if __name__ == "__main__":

    #board = MultiWii("/dev/ttyUSB0")
    board = MultiWii("/dev/tty.SLAB_USBtoUART")
    try:
        while True:
            board.getData(MultiWii.RAW_IMU)
            #print (board.attitude) #uncomment for regular printing

            # Fancy printing (might not work on windows...)
            message = "ax = {:+.0f} \t ay = {:+.0f} \t az = {:+.0f} gx = {:+.0f} \t gy = {:+.0f} \t gz = {:+.0f} mx = {:+.0f} \t my = {:+.0f} \t mz = {:+.0f} \t elapsed = {:+.4f} \t" .format(float(board.rawIMU['ax']),float(board.rawIMU['ay']),float(board.rawIMU['az']),float(board.rawIMU['gx']),float(board.rawIMU['gy']),float(board.rawIMU['gz']),float(board.rawIMU['mx']),float(board.rawIMU['my']),float(board.rawIMU['mz']),float(board.attitude['elapsed']))
            stdout.write("\r%s" % message )
            stdout.flush()
            # End of fancy printing
    except Exception,error:
        print ("Error on Main: "+str(error))
