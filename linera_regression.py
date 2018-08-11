# encoding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import sys

'''
梯度下降算法实现
'''


X = [1,2,3,4,5,9,10]
Y = [2.4,3.1,3.9,3.8,3.6,7.3,9.0]

t0 = 0.
t1 = 1.

def h(x):
    global t0, t1
    return t0+t1*x

def J0(x, y):
    j = []
    for i in range(len(x)):
        j.append(h(x[i])-y[i])
    return sum(j)/len(j)

def J1(x, y):
    j = []
    for i in range(len(x)):
        j.append((h(x[i])-y[i])*x[i])
    return sum(j)/len(j)

def gdescent(x, y, a=0.01):
    '''
    a: 步长
    '''
    global t0, t1

    tmp0 = t0 - a * J0(x, y)
    tmp1 = t1 - a * J1(x, y)
    print(tmp0,tmp1)
    dg = sqrt((tmp0-t0)*(tmp0-t0)+(tmp1-t1)*(tmp1-t1)) 
    t0 = tmp0
    t1 = tmp1
    return dg

dg = sys.maxsize
step = 1
# 迭代次数不超过 1000
for itn in range(1000):
    # 步长过大，可能导致不收敛
    ndg = gdescent(X, Y, step)
    if ndg > dg: # 不收敛，步长太大
        step = step / 10
    dg = ndg
    print(dg)
    if (dg < step/2): # 假定下降小于步长一半
        print("迭代次数 = ", itn)
        break

print(t0, t1)



plt.title('梯度下降')

# 画图
# 1.真实的点
plt.scatter(X, Y, color='blue')
 
# 2.拟合的直线
plt.plot(X, [ (t0 + t1 * n) for n in X ], color='red')

plt.show()