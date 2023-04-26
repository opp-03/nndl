# -*- coding: utf-8 -*-
"""RLSKT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14Jy-hAsv5nweMhxof-ehXKqrGNhwdraT
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense,Dropout,LSTM

mnist = tf.keras.datasets.mnist
(x_train , y_train),(x_test , y_test)= mnist.load_data()

print(x_train.shape)
print(x_train[0].shape)

from IPython.core import macro
model = Sequential()
model.add(LSTM(128 , input_shape=(x_train.shape[1:]),activation='relu',return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.1))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

opt = tf.keras.optimizers.legacy.Adam(lr=0.001,decay=1e-6)
model.compile(
     loss='sparse_categorical_crossentropy',
     optimizer = opt,
     metrics=['accuracy'],
     )


model.fit(x_train,
          y_train,
          epochs =3,
          validation_data=(x_test , y_test))

_, accuracy = model.evaluate(x_test, y_test)
print('Accuracy: %.2f' % (accuracy*100))