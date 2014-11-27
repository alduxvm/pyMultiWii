#!/usr/bin/env python

"""main.py: Main module to control a multicopter."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"


import serial, struct, time, threading, SocketServer
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import cfg, MSP, optiUDP


if __name__ == "__main__":

    try:

        if cfg.DRONE:
            MSP.startMulticopter()
            readThread = threading.Thread(target=MSP.getDataInf, args=(MSP.ATTITUDE,))
            readThread.start()

        if cfg.SCKSRV:
            server = SocketServer.UDPServer((cfg.UDPip, cfg.UDPport), optiUDP.optiUDPserver)
            UDPthread = threading.Thread(target=server.serve_forever, name="SocketServer Loop")
            UDPthread.start()

        if cfg.ASY:
            optiUDP.AsyncoreServerUDP()
            UDPthread = threading.Thread(target=optiUDP.asyncore.loop, name="Asyncore Loop")
            UDPthread.start()

        if cfg.PRINT:
            printThread = threading.Timer(0.02,cfg.manageData)
            printThread.start()

        if cfg.TWIS:
            optiUDP.startTwisted()
        
          
    except Exception,error:
        print "Error: "+str(error)
        MSP.ser.close()