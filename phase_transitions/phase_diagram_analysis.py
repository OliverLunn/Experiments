import numpy as np
import matplotlib.pyplot as plt

path="videos/07_31_area_f_0.556/"

#load in acc data + duty cycles + counts 
data1 = np.loadtxt(path+"data_1.txt", dtype=float)
data2 = np.loadtxt(path+"data_2.txt", dtype=float)
data3 = np.loadtxt(path+"data_3.txt", dtype=float)
data4 = np.loadtxt(path+"data_4.txt", dtype=float)
data5 = np.loadtxt(path+"data_5.txt", dtype=float)

acc_1 = np.loadtxt(path+"acceleration_data_1.txt", dtype=float)
acc_2 = np.loadtxt(path+"acceleration_data_2.txt", dtype=float)
acc_3 = np.loadtxt(path+"acceleration_data_3.txt", dtype=float)
acc_4 = np.loadtxt(path+"acceleration_data_4.txt", dtype=float)
acc_5 = np.loadtxt(path+"acceleration_data_5.txt", dtype=float)

#stack data columns
order_data = np.stack((data1[:,0], data2[:,0], data3[:,0], data4[:,0], data5[:,0]), axis=1)
acc_data = np.stack((acc_1, acc_2, acc_3, acc_4, acc_5), axis=1)
duty_data = np.stack((data1[:,1], data2[:,1], data3[:,1], data4[:,1], data5[:,1]), axis=1)
area_fraction = np.stack((data1[:,2], data2[:,2], data3[:,2], data4[:,2], data5[:,2]), axis=1)

#calc mean and std
mean_order = np.mean(order_data, axis=1)
std_order = np.std(order_data, axis=1)
mean_duty = np.mean(duty_data, axis=1)
std_duty = np.std(duty_data, axis=1)
mean_acc = np.mean(acc_data, axis=1)
std_acc = np.std(acc_data, axis=1)

mean_area_fraction = np.mean(area_fraction)
std_area_frac = np.std(area_fraction)

#plotting
fig, (ax1) = plt.subplots(1,1, figsize=(10,8), sharey=False)
ax1.errorbar(mean_acc[1:], mean_order[1:], yerr=std_order[1:], fmt="bd", ecolor="k", capsize=1)
ax1.set_xlabel("Acceleration $\Gamma$", fontsize=20)
ax1.set_ylabel("|$\Psi_6$|", fontsize=20)
ax1.text(4.2,0.75,"$\phi$: {:.3f}".format(mean_area_fraction)+"$+/-${:.3f}".format(std_area_frac),fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()