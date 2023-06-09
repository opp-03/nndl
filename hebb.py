# -*- coding: utf-8 -*-
"""hebb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r8HLtkCyGV94TQEPDOWewbzSi2xIgKiN
"""

import numpy as np
import pandas as pd

W=np.array([1,-1,0,0.5]).transpose()
Xi=[np.array([1,-2,1.5,0]).transpose(),np.array([1,-0.5,-2,-1.5]).transpose(),np.array([0,1,-1,1.5]).transpose()]
C=1
Iteration=0
print(W)
print(Xi)

for i in range (len(Xi)):
  net=sum (W.transpose()*Xi[1])
  Fnet=np.sign(net)
  dw=C*Fnet*Xi[i]
  W= W+dw
  print("Weight vector for this iteration:",W)
  Iteration +=1

print('Final weight materix:',W)
print('Number of iteration:', Iteration)