from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt
n = 60000 # number of samples
(minValue, maxValue) = (1, 6)
x = randint(minValue, maxValue+1, n)
diceOutput = np.zeros((1,maxValue), np.uint32)
print(f"Zar {n} defa atıldı.")
for i in range(maxValue):
    diceOutput[0,i] = np.count_nonzero(x == i+1)
    print(f"Zar {diceOutput[0,i]} defa {i+1} geldi --> {diceOutput[0,i]}/{n} = {diceOutput[0,i]/n}")
print("A: 2'den büyük gelme olasılığı")
print(f"P(A) = {(diceOutput[0,2]+diceOutput[0,3]+diceOutput[0,4]+diceOutput[0,5])/n}")
counts, edges, bars = plt.hist(x, bins=np.arange(minValue-0.5,maxValue+1.5,1), 
         color='gray', histtype='bar')
plt.bar_label(bars)
plt.title(f"Toplam {n} kez zar atıldığında oluşan histogram")
plt.xlabel("Örneklem uzay --> S = {1,2,3,4,5,6}")
plt.ylabel("Sayaç")
plt.show()