import numpy as np
import matplotlib.pyplot as plt

data_1 = np.loadtxt("phase_transitions/phase_diagram/order_acc_0.516.txt")
data_2 = np.loadtxt("phase_transitions/phase_diagram/order_acc_0.599.txt")
data_3 = np.loadtxt("phase_transitions/phase_diagram/order_acc_0.645.txt")
data_4 = np.loadtxt("phase_transitions/phase_diagram/order_acc_0.686.txt")

mean_order_1, std_order_1, mean_acc_1 = data_1[0,:], data_1[1,:], data_1[2,:]
mean_order_2, std_order_2, mean_acc_2 = data_2[0,:], data_2[1,:], data_2[2,:]
mean_order_3, std_order_3, mean_acc_3 = data_3[0,:], data_3[1,:], data_3[2,:]
mean_order_4, std_order_4, mean_acc_4 = data_4[0,:], data_4[1,:], data_4[2,:]
fig, (ax1) = plt.subplots(1,1, figsize=(12,8), sharey=False)

ax1.errorbar(mean_acc_1[1:], mean_order_1[1:], yerr=std_order_1[1:], fmt="b^", ecolor="k", capsize=1, label="$\phi$=0.516")
ax1.errorbar(mean_acc_2[1:], mean_order_2[1:], yerr=std_order_2[1:], fmt="r^", ecolor="k", capsize=1, label="$\phi$=0.599")
ax1.errorbar(mean_acc_3[1:], mean_order_3[1:], yerr=std_order_3[1:], fmt="k^", ecolor="k", capsize=1, label="$\phi$=0.645")
ax1.errorbar(mean_acc_4[1:], mean_order_4[1:], yerr=std_order_4[1:], fmt="g^", ecolor="k", capsize=1, label="$\phi$=0.686")
ax1.set_xlabel("Acceleration $\Gamma$", fontsize=20)
ax1.set_ylabel("|$\Psi_6$|", fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(fontsize="xx-large")
plt.show()