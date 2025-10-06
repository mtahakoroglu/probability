from numpy.random import rand
T = 60 # 1 saatlik bir zaman penceresi
w = 15 # 15 dk bekleme süresi
n = 50000 # toplam örnek (sample) sayısı
xy = T*rand(n,2) # n adet rasgele örnek üret
m = sum(abs(xy[:,0]-xy[:,1]) <= w) # buluşulan örnek sayısı
print('Olasılık (analitik) %.5f' %((T**2-(T-w)**2)/(T**2)))
print('Olasılık (nümerik) %.5f' %(m/n))
