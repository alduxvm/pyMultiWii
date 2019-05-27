from pymultiwii import MultiWii
import time
#serialPort = "/dev/ttyAMA0"
serialPort = "/dev/tty.SLAB_USBtoUART"
board = MultiWii(serialPort)
print("woken up")
#board.sendCMD(0,MultiWii.REBOOT,[],'')
time.sleep(1)
board.setVTX(5,5,1)
time.sleep(3)
test = board.getData(MultiWii.ATTITUDE)
print(test)

while True :
    test = board.getData(MultiWii.ATTITUDE)
    #print board.getData(MultiWii.STATUS)
    print(board.getData(MultiWii.VTX_CONFIG))
    test = 1
