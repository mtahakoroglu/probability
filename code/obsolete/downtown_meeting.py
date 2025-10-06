from numpy.random import rand
import matplotlib.pyplot as plt
n = 1000 # örnek sayısı
T = 60
w = 15 # zamanda bekleme penceresi
xy = T*rand(n,2)
# print(xy)
count = 0 # buluşmaları sayıyoruz
for i in range(n):
    if ( abs(xy[i,0] - xy[i,1]) <= w ):
        count = count + 1
        plt.scatter(xy[i,0],xy[i,1],c="red")
    else:
        plt.scatter(xy[i,0],xy[i,1],c="blue")
print(f"Buluşma olasılıkları gerçekte {(T**2 - (T-w)**2) / (T**2)} simülasyonda {count/n}")
plt.show()