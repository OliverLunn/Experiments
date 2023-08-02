import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt



phi = np.array([0.516,0.552,0.555,0.573,0.5986,0.602,0.636,0.645,0.649,0.67,0.686])
gamma = np.array([3.3565,3.4231,3.2201,3.4627,3.5005,3.5863,3.7152,3.7947,3.8126,3.9257,4.0325])
midpoint = np.array([0.7158, 0.7009, 0.60519,0.6764, 0.6802, 0.663, 0.6456, 0.6075, 0.58112, 0.63711, 0.591])

fig, (ax) = plt.subplots(1,1,figsize=(12,8))


ax.plot(phi,gamma, "kD",markersize=4)
ax.set_ylabel("$\phi$", fontsize=20)
ax.set_xlabel("$\Gamma$", fontsize=20)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
