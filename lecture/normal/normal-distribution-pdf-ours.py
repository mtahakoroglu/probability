import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 50, 5
xmin, xmax, T = mu - 4*sigma, mu + 4*sigma, 0.01
x = np.arange(xmin, xmax+T, T)
f = (1/np.sqrt(2 * np.pi * sigma**2)) * np.exp(- (x - mu)**2 / (2 * sigma**2))
# Monte Carlo Simülasyonu da yapalım
n = 10_000
samples = np.random.normal(mu, sigma, n)
# 45-55 arasında olma olasılığını histogramdan bulalım
count_45_55 = ((samples >= 45) & (samples <= 55)).sum() / n

# Grafik çizdirme
plt.plot(x, f, color="red", label="Normal Dağılım PDF")
plt.hist(samples, bins=50, density=True, alpha=0.6, 
         label=f"MCS (nümerik çözüm)")
plt.title(f"MCS çözümü P(45<X<55)={count_45_55}")
plt.xlabel("x Değerleri")
plt.ylabel("Olasılık Yoğunluğu")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper right")
plt.savefig("normal_distribution_MCS.png", dpi=300)
plt.show()