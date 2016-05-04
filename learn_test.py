# -*- coding: utf-8　-*-
import csv   #csvモジュールをインポートする
import numpy as np
import serial
import sys
from numpy import *
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

#ラベル
f = open('lavel.csv', 'rb')
dataReader = csv.reader(f)
lista = []
for row in dataReader:
    lista.append(','.join(row))

#学習データ
X = np.loadtxt('data.csv', delimiter=',', dtype='float')
y = lista #クラスラベル

#clf = svm.SVC(kernel='rbf') #Support Vector Classification(分類)、RBFカーネルを使用
#clf.fit(X, y) #学習
model = RandomForestClassifier()
model.fit(X, y)

#識別するところ
ser = serial.Serial("/dev/cu.usbserial-AH01ASKQ",9600)
ser.open
while True:
    data = ser.readline().strip().rsplit()
    data.pop(0)
    print data
    output = model.predict(data)
    print(output)
f.close
ser.close
