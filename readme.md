Arduinoで測距センサを4つ，加速度センサを１つ接続したものを用意
収集したセンサデータを元に行動推定を行うプログラムです．

実装したものの精度的には加速度センサは無い方がよい感じなので削ってあります

make_learn_data.pyでセンサの値を収集．
learn_test.py　で機械学習と推定を行っています．

gitに上げたのがプログラムを作ってから半年以上たってますのでファイル名関係はうろ覚えです．