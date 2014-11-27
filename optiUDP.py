#!/usr/bin/env python

"""optiUDP.py: Handles UDP SocketServer communications for reading a Optitrack Motion Capture System."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2014 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"


import struct, time, SocketServer, asyncore, socket
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import cfg

UDPmess = ();
UDPtimestamp = 0

class optiUDPserver(SocketServer.BaseRequestHandler):

    def handle(self):
        global UDPmess, UDPmess2
        UDPmess=();
        numOfValues=0
        timestamp = time.time()
        data = self.request[0].strip()
        try:
            numOfValues = len(data) / 8
            mess=struct.unpack('>' + 'd' * numOfValues, data)
            UDPmess=mess
            #udp_mess2=udp_mess
        except Exception,error:
            #print "SocketServer: "+str(error)
            pass


class AsyncoreServerUDP(asyncore.dispatcher):
    def __init__(self):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.set_reuse_addr()
        self.bind((cfg.UDPip, cfg.UDPport))
    
    # Even though UDP is connectionless this is called when it binds to a port
    def handle_connect(self):
        print "Server Started..."
    
    # This is called everytime there is something to read
    def handle_read(self):
        global UDPmess 
        global UDPmess2
        udp_mess=""
        data, addr = self.recvfrom(1024)
        numOfValues = len(data) / 8
        mess=struct.unpack('>' + 'd' * numOfValues, data)
        UDPmess=mess

   # This is called all the time and causes errors if you leave it out.
    def handle_write(self):
        pass


class twistedUDP(DatagramProtocol):

    def datagramReceived(self, data, (host, port)):
        global UDPmess
        numOfValues = len(data) / 8
        mess=struct.unpack('>' + 'd' * numOfValues, data)
        UDPmess = [ round(element,4) for element in mess ]
        UDPmess.insert(0,time.time())

def startTwisted():
    reactor.listenUDP(cfg.UDPport, twistedUDP())
    reactor.run()