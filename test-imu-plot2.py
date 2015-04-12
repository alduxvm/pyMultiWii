#!/usr/bin/env python

"""test-imu-plot.py: Ask multiwii for raw IMU and plot it using pyqtgraph."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2015 Aldux.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pyMultiwii import MultiWii

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

board = MultiWii("/dev/tty.usbserial-A801WZA1")
win = pg.GraphicsWindow()
win.setWindowTitle('MultiWii IMU plotting')

p1 = win.addPlot()
win.nextRow()
p2 = win.addPlot()
data1 = [0] * 300
data2 = [0] * 300
data3 = [0] * 300
data4 = [0] * 300
data5 = [0] * 300
data6 = [0] * 300
curve1 = p1.plot(data1, name="ax", pen=(255,0,0))
curve2 = p1.plot(data2, name="ay", pen=(0,255,0))
curve3 = p1.plot(data3, name="az", pen=(0,0,255))
curve4 = p2.plot(data1, name="gx", pen=(255,0,0))
curve5 = p2.plot(data2, name="gy", pen=(0,255,0))
curve6 = p2.plot(data3, name="gz", pen=(0,0,255))
def update1():
    global data1, curve1, board
    board.getData(MultiWii.RAW_IMU)
    t = float(board.rawIMU['timestamp'])
    ax = board.rawIMU['ax']
    ay = board.rawIMU['ay']
    az = board.rawIMU['az']
    gx = board.rawIMU['gx']
    gy = board.rawIMU['gy']
    gz = board.rawIMU['gz']

    data1[:-1] = data1[1:]  
    data1[-1] = ax
    data2[:-1] = data2[1:]  
    data2[-1] = ay
    data3[:-1] = data3[1:]  
    data3[-1] = az
    data4[:-1] = data4[1:]  
    data4[-1] = gx
    data5[:-1] = data5[1:]  
    data5[-1] = gy
    data6[:-1] = data6[1:]  
    data6[-1] = gz
    curve1.setData(data1)
    curve2.setData(data2)
    curve3.setData(data3)
    curve4.setData(data4)
    curve5.setData(data5)
    curve6.setData(data6)
    

def update():
    update1()
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
