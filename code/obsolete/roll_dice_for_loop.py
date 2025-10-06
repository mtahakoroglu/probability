from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt

n = 600 # number of samples
(minValue, maxValue) = (1, 6)
x = randint(minValue, maxValue+1, n)
diceOccurrence = np.zeros((1,maxValue), np.uint32)
print(f"Zar {n} defa atıldı.")
for i in range(maxValue):
    diceOccurrence[0,i] = np.count_nonzero(x == i+1)
    print(f"Zar {diceOccurrence[0,i]} defa {i+1} geldi.")
plt.hist(x, [0.5,1.5,2.5,3.5,4.5,5.5,6.5])
plt.show()