import numpy as np
import matplotlib.pyplot as plt

path="videos/2023_07_28_hysteresis/rate_2/"

#load in acc data + duty cycles + counts 
data1c = np.loadtxt(path+"data_1c.txt", dtype=float)
data2c = np.loadtxt(path+"data_2c.txt", dtype=float)
data3c = np.loadtxt(path+"data_3c.txt", dtype=float)

data1h = np.loadtxt(path+"data_1h.txt", dtype=float)
data2h = np.loadtxt(path+"data_2h.txt", dtype=float)
data3h = np.loadtxt(path+"data_3h.txt", dtype=float)

acc_1c = np.loadtxt(path+"acceleration_data_1c.txt", dtype=float)
acc_2c = np.loadtxt(path+"acceleration_data_2c.txt", dtype=float)
acc_3c = np.loadtxt(path+"acceleration_data_3c.txt", dtype=float)

acc_1h = np.loadtxt(path+"acceleration_data_1h.txt", dtype=float)
acc_2h = np.loadtxt(path+"acceleration_data_2h.txt", dtype=float)
acc_3h = np.loadtxt(path+"acceleration_data_3h.txt", dtype=float)

#stack data columns
order_data_c = np.stack((data1c[:,0], data2c[:,0], data3c[:,0]), axis=1)
acc_data_c = np.stack((acc_1c, acc_2c, acc_3c), axis=1)
order_data_h = np.stack((data1h[:,0], data2h[:,0], data3h[:,0]), axis=1)
acc_data_h = np.stack((acc_1h, acc_2h, acc_3h), axis=1)

area_fraction = np.stack((data1c[:,2], data2c[:,2], data3c[:,2]), axis=1)
#calc mean and std
mean_order_c = np.mean(order_data_c, axis=1)
std_order_c = np.std(order_data_c, axis=1)
mean_acc_c = np.mean(acc_data_c, axis=1)
std_acc_c = np.std(acc_data_c, axis=1)

mean_order_h = np.mean(order_data_h, axis=1)
std_order_h = np.std(order_data_h, axis=1)
mean_acc_h = np.mean(acc_data_h, axis=1)
std_acc_h = np.std(acc_data_h, axis=1)

mean_area_fraction = np.mean(area_fraction)
std_area_frac = np.std(area_fraction)

#plotting
fig, (ax2) = plt.subplots(1,1, sharey=False)

ax2.errorbar(mean_acc_c[1:], mean_order_c[1:], yerr=std_order_c[1:], fmt="bo", ecolor="k", capsize=1)
ax2.errorbar(mean_acc_h[1:], mean_order_h[1:], yerr=std_order_h[1:], fmt="ro", ecolor="k", capsize=1)

ax2.set_xlabel("Acceleration $\Gamma$")
ax2.set_ylabel("$\Psi_6$")
ax2.set_title("Area fraction:{:.3f}".format(mean_area_fraction)+"$+/-${:.3f}".format(std_area_frac))

plt.show()