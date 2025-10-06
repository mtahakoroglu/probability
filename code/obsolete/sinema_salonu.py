from numpy.random import randint
import numpy as np
n = 50000
m = 0
xy = randint(1,101,(n,2))
for i in range(n):
    while xy[i,0] == xy[i,1]:
        xy[i,1] = randint(1,101)
    if (abs(xy[i,0]-xy[i,1]) == 1) and (np.ceil(xy[i,0]/10) == np.ceil(xy[i,1]/10)):
        m += 1
print('Yan yana oturma olasılığı (analitik) = %.5f' %(1/55))
print('Yan yana oturma olasılığı (nümerik) = %.5f' %(m/n))