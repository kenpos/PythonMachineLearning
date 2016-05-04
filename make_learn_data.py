#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import serial
import sys
import time
from time import time

def save():
    threading.currentThread().getName()
    t=threading.Timer(1,save)
    t.start()


def main():
    value = 0
    #Get value from Arduino
    ser = serial.Serial("/dev/cu.usbserial-AH01ASKQ",9600)
    ser.open
    dataFile = open('data.csv','a')
    lavelFile = open('lavel.csv','a')
    dataWriter = csv.writer(dataFile, lineterminator='\n')
    lavelWriter = csv.writer(lavelFile, lineterminator='\n')

    print "学習のためのトレーニングデータを集めます．"
    print "表示されている動きをしてください．"
    print "start:開始   stop:終了"
    input_data = raw_input('>>> ')
    print "学習中...."
    move = ['Neutral',"Force"]
    cnt = 0
    while True:
        print input_data
        if input_data == 'stop':break
        print "2秒で次の動作に移行します."
        print move[cnt % len(move)]
             #学習データ収集
        start = time()
        while True:
            end = time()
            if end - start >= 4:
                print("次の工程に移ります\n")
                start = time()
                while True:
                    if end - start >= 1:
                        end = time()
                    break
                break
            ser.write("*".encode())
            data = ser.readline().strip().rsplit()
            data.pop(0)
            dataWriter.writerow(data)
            print data
            lavelWriter.writerow(move[cnt % len(move)].strip().rsplit())
        cnt += 1
        if cnt == 12 :break
    ser.close()
    dataFile.close()
    lavelFile.close()


if __name__ == '__main__':
    main()
