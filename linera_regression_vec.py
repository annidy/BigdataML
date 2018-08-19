# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import sys

'''
梯度下降算法实现
线性代数
'''

X = [1,2,4,6]
Y = [0.8,1.3,1.9,5]

m = len(X)
theta = np.array([[0], [1]])
one = np.ones(m)
VX = np.vstack((one, X)).T
VY = np.array(Y).reshape(m,1)

for itn in range(1000):
    a = 0.01
    # deleta = ((theta.T * VX.T- VY).T @ VX).T
    deleta = ((VX @ theta - VY).T @ VX).T / m
    theta = theta - a * deleta 
    if np.all(deleta < a/10):
        break

print(theta)

plt.scatter(X, Y, color='blue')
x = np.array(X)
plt.plot(x,  VX @ theta, color='red', label='linera')

plt.show()