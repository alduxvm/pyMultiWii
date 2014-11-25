#!/usr/bin/env python

"""cfg.py: Configuration file."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"


import serial

"""General settings"""
PRINT   =   1   # Print data to terminal, useful for debugging
FILE    =   0   # Save to a timestamped file, the data selected below
TIME    =   1   # Save the difference of time between all the main functions for perfomance logging
FLYT    =   0   # Save the flight time in seconds
ATT     =   0   # Ask and save the attitude of the multicopter
ALT     =   0   # Ask and save the altitude of the multicopter
RC      =   1   # Ask and save the pilot commands of the multicopter
MOT     =   0   # Ask and save the PWM of the motors that the MW is writing to the multicopter
RAW     =   0   # Ask and save the raw imu data of the multicopter
RCRAW   =   0   # Ask and save the rc & raw imu data of the multicopter
CMD     =   0   # Send commands to the MW to control it
UDP     =   0   # Save or use UDP data (to be adjusted)
ASY     =   0   # Use async communicacion
SCK     =   0   # Use regular socket communication
SCKSRV  =   0   # Use socketserver communication


"""Serial Port Configuration for easy access"""
#port = "/dev/tty.usbserial-AM016WP4" # This is the port that the MultiWii is attached to (for mac & MW home)
port = "/dev/tty.usbserial-A101CCVF"  # This is the port that the MultiWii is attached to (for mac & MW office)
#port = "/dev/ttyUSB0"    # This is the port that the MultiWii is attached to (for raspberry pie)


