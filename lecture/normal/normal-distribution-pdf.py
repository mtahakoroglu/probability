import numpy as np
import matplotlib.pyplot as plt

T = 0.01
x = np.arange(-6, 6+T, T)
# mu1, mu2, mu3, mu4 = 0, 0, 0, -2
mu = np.array([0, 0, 0, -2])
# sigma1, sigma2, sigma3, sigma4 = 1, 0.5, 2, 1
sigma = np.array([1, 0.5, 2, 1])

def normal_pdf(x, mu, sigma):
    coef = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coef * np.exp(exponent)

y = [normal_pdf(x, mu[i], sigma[i]) for i in range(4)]
plt.plot(x, y[0], label=fr"$\mu={mu[0]}, \sigma={int(sigma[0])}$")
plt.plot(x, y[1], label=fr"$\mu={mu[1]}, \sigma={sigma[1]}$")
plt.plot(x, y[2], label=fr"$\mu={mu[2]}, \sigma={int(sigma[2])}$")
plt.plot(x, y[3], label=fr"$\mu={mu[3]}, \sigma={int(sigma[3])}$")
plt.title("Normal Dağılım PDF", fontsize=15)
plt.xlabel("x", fontsize=15)
plt.ylabel(r"$f_X(x)$", fontsize=18)
plt.legend(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xlim(-6, 6)
plt.savefig("normal_distribution_pdf.png", dpi=400)
plt.show()

# y1 = normal_pdf(x, mu1, sigma1)
# y2 = normal_pdf(x, mu2, sigma2)
# y3 = normal_pdf(x, mu3, sigma3)
# y4 = normal_pdf(x, mu4, sigma4)