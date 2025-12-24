import numpy as np
import matplotlib.pyplot as plt

# plot exponential pdf and also make MCS
def exponential_pdf(lam, x):
    return lam * np.exp(-lam * x)

def plot_exponential_with_mcs(lam, num_samples=1_000):
    # Monte Carlo Simulation
    samples = np.random.exponential(1/lam, num_samples)
    xmin, xmax, T = 0, np.max(samples)+1, 0.1
    # Generate x values
    x = np.arange(xmin, xmax, T)
    y = exponential_pdf(lam, x)
    # Plotting
    plt.plot(x, y, 'r-', lw=1.5, label='Üstel dağılım', color='red')
    # bin'ler üzerine sayım değerlerini ekleme
    counts, bin_edges = np.histogram(samples, bins=np.arange(0, np.ceil(max(samples))+1, 1))
    plt.hist(samples, bins=np.arange(0, np.ceil(max(samples))+1, 1), density=True, alpha=0.5, label='MCS Samples', color='gray', edgecolor='black')
    # Her bin üzerine sayım değerlerini ekleme
    for count, edge in zip(counts, bin_edges):
        if count > 0:
            plt.text(edge + 0.5, count/num_samples, str(count), ha='center', va='bottom', fontsize=10)
    print(np.arange(0, np.ceil(max(samples))+1, 1))
    print(f"max(samples) -->  np.ceil(max(samples))+1 : {max(samples)} -->  {np.ceil(max(samples))+1}")
    plt.title(f'Üstel dağılım Monte Carlo Simülasyonu (n={num_samples})')
    plt.xlabel('Zaman [dk]')
    plt.ylabel('Gözlem Yoğunluğu')
    plt.grid()
    plt.legend()
    plt.show()
    
# Example usage
plot_exponential_with_mcs(lam=0.8, num_samples=10_000)