#!/usr/bin/env python

"""test-imu-plot.py: Ask multiwii for raw IMU and plot it using matplotlib."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2016 Altax.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pymultiwii import MultiWii

import time
import matplotlib.pyplot as plt

class Chart(object):
	def __init__(self):
		self.senses = 0
		self.sb, self.axbuf, self.aybuf, self.azbuf = 0, 0, 0, 0
		self.gxbuf, self.gybuf, self.gzbuf = 0, 0, 0
		plt.show(block=False)
		plt.ion()
		self.fig = plt.figure(1, figsize=(19, 6))
		plt.ylim([-1000, 1000])
		plt.xlim([0, 300])
 
	def plot(self, ax, ay, az, gx, gy, gz):
		self.senses += 1
		plt.plot([self.sb, self.senses], [self.axbuf, ax], color='r', label='AX')
		plt.plot([self.sb, self.senses], [self.aybuf, ay], color='g', label='AY')
		plt.plot([self.sb, self.senses], [self.azbuf, az], color='b', label='AZ')
		plt.plot([self.sb, self.senses], [self.gxbuf, gx], color='y', label='GX')
		plt.plot([self.sb, self.senses], [self.gybuf, gy], color='black', label='GY')
		plt.plot([self.sb, self.senses], [self.gzbuf, gz], color='pink', label='GZ')
		self.fig.canvas.draw()
		self.sb, self.axbuf, self.aybuf, self.azbuf, self.gxbuf, self.gybuf, self.gzbuf = self.senses, ax, ay, az, gx, gy, gz

if __name__ == "__main__":
	chart = Chart()
	#serialPort = "/dev/tty.usbserial-A801WZA1"
	serialPort = "/dev/tty.SLAB_USBtoUART"
	board = MultiWii(serialPort)
	
	try:
		while True:
			board.getData(MultiWii.RAW_IMU)
			#print (board.rawIMU)
			t = float(board.rawIMU['timestamp'])
			ax = board.rawIMU['ax']
			ay = board.rawIMU['ay']
			az = board.rawIMU['az']
			gx = board.rawIMU['gx']
			gy = board.rawIMU['gy']
			gz = board.rawIMU['gz']
			chart.plot(ax, ay, az, gx, gy, gz)
	except Exception,error:
		print ("Error on Main: "+str(error))