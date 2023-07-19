import numpy as np
import matplotlib.pyplot as plt

path="videos/2023_07_19_morning/"
#load in acc data + duty cycles + counts 
data1 = np.loadtxt(path+"data_1.txt", dtype=float)
data2 = np.loadtxt(path+"data_2.txt", dtype=float)
data3 = np.loadtxt(path+"data_3.txt", dtype=float)

acc_1 = np.loadtxt(path+"acceleration_data_1.txt", dtype=float)
acc_2 = np.loadtxt(path+"acceleration_data_2.txt", dtype=float)
acc_3 = np.loadtxt(path+"acceleration_data_3.txt", dtype=float)

#stack data columns
count_data = np.stack((data1[:,0], data2[:,0], data3[:,0]), axis=1)
acc_data = np.stack((acc_1, acc_2, acc_3), axis=1)
duty_data = np.stack((data1[:,1], data2[:,1], data3[:,1]), axis=1)

#calc mean and std 
mean_count = np.mean(count_data, axis=1)
std_count = np.std(count_data, axis=1)

mean_duty = np.mean(duty_data, axis=1)
std_duty = np.std(duty_data, axis=1)

mean_acc = np.mean(acc_data, axis=1)
std_acc = np.std(acc_data, axis=1)

print(np.shape(std_acc)) 

#plotting
fig, (ax1, ax2) = plt.subplots(2,1, sharey=False)

ax1.errorbar(mean_duty, mean_count, yerr=std_count, fmt=".", ecolor="k", capsize=2)
ax1.set_xlabel("Duty Cycle")
ax1.set_ylabel("$\Psi_6$")

ax2.errorbar(mean_acc[1:], mean_count[1:], yerr=std_count[1:], fmt=".", ecolor="k", capsize=2)
#ax2.plot(mean_acc[1:], mean_count[1:], ".")
#ax2.fill_between(mean_acc[1:], (mean_count[1:]-std_count[1:]/2), (mean_count[1:]+std_count[1:]/2), color="lightcyan")
ax2.set_xlabel("Acceleration $\Gamma$")
ax2.set_ylabel("$\Psi_6$")

plt.show()