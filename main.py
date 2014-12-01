#!/usr/bin/env python

"""main.py: Main module to test communication with a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from multiwii import MultiWii

if __name__ == "__main__":

  serialPort = "/dev/tty.usbserial-A101CCVF"

  board1 = MultiWii(serialPort)
  #board2 = MultiWii("/dev/tty.usbserial-AM016WP4")

  try:
    while True:

      print board1.getData(MultiWii.RAW_IMU)
      #cfg.plotData()  
  except Exception,error:
    print "Error: "+str(error)