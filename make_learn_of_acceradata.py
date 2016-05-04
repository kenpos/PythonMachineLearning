# -*- coding: utf-8 -*-
import math
import numpy as np
#センサの向きがどの方向を指しているかわかるが，もしセンサがどの向きにあったのかわからない場合，軸の持つ情報が失われてしまう．
#x,y,z座標の合成した値rを取得し，センサが受けた加速度の大きさだけが情報として残り，センサの向きに影響されずに同じ値を得ることができる．
#r = √(x^2+y^2+z^2)
data = np.loadtxt("accele.csv",delimiter=",")
print data
matrix1 = data**2
col_sum = matrix1.sum(axis=1)
r = np.sqrt(col_sum)
print r

#線形補完，センサ値の取得間隔には設定が100Hzと設定してもきっかり取得することはできない．
#取得データを一定の間隔になるように線形補完を行う必要がある．
#今回は，補完する点を
