import numpy as np
import matplotlib.pyplot as plt

#load in acc data + duty cycles
acc_1 = np.loadtxt("acceleration_data1.txt", dtype=float)
acc_2 = np.loadtxt("acceleration_data2.txt", dtype=float)
acc_3 = np.loadtxt("acceleration_data3.txt", dtype=float)
acc_4 = np.loadtxt("acceleration_data4.txt", dtype=float)
acc_5 = np.loadtxt("acceleration_data5.txt", dtype=float)
duty_cycle = np.loadtxt("duty_cycle_data.txt", dtype=float)

#stack data columns
acc_data = np.stack((acc_1, acc_2, acc_3, acc_4, acc_5), axis=1)
mean_acc_data = np.mean(acc_data, axis=1) #calc mean
std_acc_data = np.std(acc_data, axis=1) #calc st dev
print(np.shape(std_acc_data)) 

#plotting
fig, ax = plt.figure(1), plt.axes()
ax.errorbar(duty_cycle, mean_acc_data, yerr=std_acc_data,fmt=".", ecolor="k", capsize=2)
ax.set_xlabel("Duty Cycle")
ax.set_ylabel("Peak z-acceleration ($\Gamma$)")
ax.set_title("Shaker Calibration")
ax.grid(True)
plt.show()