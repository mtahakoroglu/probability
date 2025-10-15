from numpy.random import rand
T = 60 # 1s=60dk'lık bir zaman penceresi
w = 20 # bekleme süresi (dk)
n = 10000 # toplam örnek (sample) sayısı
xy = T*rand(n,2) # n adet rasgele örnek üret
m = sum( abs( xy[:,0] - xy[:,1] ) <= w ) # buluşulan örnek sayısı
print(f"Olasılık (analitik) {((T**2-(T-w)**2)/(T**2)):.5f}")
print(f"Olasılık (nümerik) {m/n:.5f}")