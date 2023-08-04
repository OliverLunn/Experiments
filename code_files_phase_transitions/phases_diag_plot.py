import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def polynomial(x,a,b,c):
    return a*x**2+b*x+c
def linear(x,a,b):
    return a*x+b

data = np.loadtxt("phase_transitions/phase_diagram_data.txt")
phi = data[0,:]
gamma = data[1,:]

fig, (ax) = plt.subplots(1,1,figsize=(12,8))

popt, pcov = opt.curve_fit(polynomial, phi, gamma)
perr = np.sqrt(np.diag(pcov))
print(perr)
ax.plot(phi, polynomial(phi, *popt), "k", linestyle="--")
ax.plot(phi,gamma,".", markersize=10)
ax.set_xlabel("Area Fraction, $\phi$", fontsize=20)
ax.set_ylabel("Dimensionless Acceleration, $\Gamma$", fontsize=20)

plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
