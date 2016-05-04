# -*- coding: utf-8 -*-
"""
センサーデータ確認用．ひたすらprintするだけ．
"""

import serial

def test():
    devPath = "/dev/cu.usbmodem1421"
    leadtime = 9600
    ser = serial.Serial(devPath, leadtime)
    ser.open

    while True:
        data = ser.readline().strip().rsplit()
        print(data)

if __name__ == "__main__":
    test()
