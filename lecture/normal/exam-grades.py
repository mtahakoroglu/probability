import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Normal dağılım parametreleri
mu = 50          # Ortalama
sigma = 5        # Standart sapma
n = 100_000      # Monte Carlo örnek sayısı

# Monte Carlo örnekleri üret
samples = np.random.normal(mu, sigma, n)

# Olasılığı Monte Carlo ile hesapla
probability = np.mean(samples < 52)

# Histogram (normalize edilmiş)
plt.hist(
    samples,
    bins=100,
    density=True,
    alpha=0.5,
    label="Monte Carlo Histogramı"
)

# Normal dağılım pdf
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = stats.norm.pdf(x, mu, sigma)
plt.plot(x, pdf, 'r-', linewidth=2, label="Normal Dağılım PDF")

# İlgilenilen bölge: X < 52
x_shade = np.linspace(mu - 4*sigma, 52, 500)
pdf_shade = stats.norm.pdf(x_shade, mu, sigma)
plt.fill_between(
    x_shade,
    pdf_shade,
    alpha=0.4,
    label=r"$P(X<52)$"
)

# Grafik ayarları
plt.xlabel("Notlar", fontsize=14)
plt.ylabel("Olasılık Yoğunluğu", fontsize=14)
plt.title(f"Monte Carlo Yaklaşımı: P(X < 52) ≈ {probability:.4f}", fontsize=14)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.xlim(mu - 4*sigma, mu + 4*sigma)
plt.savefig("exam_grades_distribution.png", dpi=400)
plt.show()