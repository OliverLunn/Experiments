import numpy as np
import matplotlib.pyplot as plt

path="videos/2023_07_27_pm/"

#load in acc data + duty cycles + counts 
data_c1 = np.loadtxt(path+"data_1.txt", dtype=float)
data_c2 = np.loadtxt(path+"data_2.txt", dtype=float)
data_c3 = np.loadtxt(path+"data_3.txt", dtype=float)

data_h1 = np.loadtxt(path+"data_4.txt", dtype=float)
data_h2 = np.loadtxt(path+"data_5.txt", dtype=float)
data_h3 = np.loadtxt(path+"data_4.txt", dtype=float)


acc_c1 = np.loadtxt(path+"acceleration_data_1.txt", dtype=float)
acc_c2 = np.loadtxt(path+"acceleration_data_2.txt", dtype=float)
acc_c3 = np.loadtxt(path+"acceleration_data_3.txt", dtype=float)

acc_h1 = np.loadtxt(path+"acceleration_data_4.txt", dtype=float)
acc_h2 = np.loadtxt(path+"acceleration_data_5.txt", dtype=float)
acc_h3 = np.loadtxt(path+"acceleration_data_5.txt", dtype=float)


#stack data columns
count_data_c = np.stack((data_c1[:,0], data_c2[:,0], data_c3[:,0]), axis=1)
count_data_h = np.stack((data_h1[:,0], data_h2[:,0], data_h3[:,0]), axis=1)

acc_data_c = np.stack((acc_c1, acc_c2, acc_c3), axis=1)
acc_data_h = np.stack((acc_h1, acc_h2, acc_h3), axis=1)

area_fraction = np.stack((data_c1[:,2], data_c2[:,2], data_c3[:,2]), axis=1)

#calc mean and std 
mean_count_c = np.mean(count_data_c, axis=1)
std_count_c = np.std(count_data_c, axis=1)
mean_count_h = np.mean(count_data_h, axis=1)
std_count_h = np.std(count_data_h, axis=1)

mean_acc_c = np.mean(acc_data_c, axis=1)
std_acc_c = np.std(acc_data_c, axis=1)
mean_acc_h = np.mean(acc_data_h, axis=1)
std_acc_h = np.std(acc_data_h, axis=1)

mean_area_fraction = np.mean(area_fraction)
std_area_frac = np.std(area_fraction)

#plotting
fig, (ax2) = plt.subplots(1,1, sharey=False)
'''
ax1.errorbar(mean_duty, mean_count, yerr=std_count, fmt="bd", ecolor="k", capsize=1)
ax1.set_xlabel("Duty Cycle")
ax1.set_ylabel("$\Psi_6$")
'''
ax2.errorbar(mean_acc_c[1:], mean_count_c[1:], yerr=std_count_c[1:], fmt="bd", ecolor="k", capsize=1)
ax2.errorbar(mean_acc_h[1:], mean_count_h[1:], yerr=std_count_h[1:], fmt="rd", ecolor="k", capsize=1)
ax2.set_xlabel("Acceleration $\Gamma$", fontsize=18)
ax2.set_ylabel("$\Psi_6$", fontsize=18)
ax2.set_title("Area fraction:{:.3f}".format(mean_area_fraction)+"$+/-${:.3f}".format(std_area_frac))
plt.show()

