# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import sys

'''
Normal equation
'''


X = np.array([1,2,4,6])
Y = np.array([0.8,1.3,1.9,5])

X1 = np.vstack((np.ones(len(X)), X)).T

# use pinv instead of inv
t = np.linalg.pinv(X1.T @ X1) @ X1.T @ Y


plt.title('')

# 画图
# 1.真实的点
plt.scatter(X, Y, color='blue')
 
# 2.拟合的直线
plt.plot(X,  X1 @ t, color='red')

plt.show()