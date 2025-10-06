import matplotlib.pyplot as plt
import numpy as np
#fixing the seed for reproducibility of the result
np.random.seed(10)
size = 100
sample = np.random.exponential(1.5, size)
bin = np.arange(0,10,1)

plt.hist(sample, bins=bin, edgecolor='blue') 
plt.title("Exponential Distribution") 
plt.show()

