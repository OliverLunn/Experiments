import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt



phi = np.array([0.686, 0.670, 0.649, 0.645, 0.636, 0.602, 0.573, 0.516, 0.5986, 0.552, 0.555, 0.6235, 0.618, 0.635])
gamma = np.array([4.0325, 3.9275, 3.7947, 3.8126, 3.7152, 3.5005, 3.4627, 3.3565, 3.5863, 3.4231, 3.4902, 3.6831, 3.6602, 3.8094])

fig, (ax) = plt.subplots(1,1,figsize=(12,8))
ax.plot(phi,gamma, "kD",markersize=4)
ax.set_xlabel("$\phi$", fontsize=20)
ax.set_ylabel("$\Gamma$", fontsize=20)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
