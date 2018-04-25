import matplotlib.pyplot as plt 
import numpy as np 
mu=0.5
sigma=0.5
distro2 = np.random.logistic(mu,sigma, 10000)
plt.hist(distro2, 50, normed=True)
distro = np.random.normal(mu, sigma, 10000)
plt.hist(distro, 50, normed=True)
plt.show()