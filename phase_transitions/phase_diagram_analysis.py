import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spy

path="videos/07_31_area_f_0.631/"

def linear(x,a,b):
    return a*x+b

def cubic(x,a,b,c,d):
    '''
    3rd order polynomial fit function
    '''
    return a*x**3+b*x**2+c*x+d

def quintic(x,a,b,c,d,e,f):
    '''
    5th order polynomial fit function
    '''
    return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f

def flipped_cubic(x,a,b,c,d):
    return (1-(a*x**3+b*x**2+c*x+d))**3

def order_mid(ydata):
    '''
    Calculates the middle of the global order parameter data
    '''
    global_order_mid = (max(ydata)-min(ydata)) / 2 + min(ydata)
    return global_order_mid

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

LOWER_BOUND = int(len(mean_acc[1:])/5)
UPPER_BOUND = int(4*len(mean_acc[1:])/5)
#popt, pcov = spy.curve_fit(quintic, mean_acc[LOWER_BOUND:UPPER_BOUND], mean_order[LOWER_BOUND:UPPER_BOUND]) #perform least-squares fit on data
midpoint_order = order_mid(mean_order[1:])

#plotting
fig, (ax1) = plt.subplots(1,1, figsize=(12,8), sharey=False)
ax1.errorbar(mean_acc[1:], mean_order[1:], yerr=std_order[1:], fmt="bd", ecolor="k", capsize=1)
ax1.set_xlabel("Acceleration $\Gamma$", fontsize=20)
ax1.set_ylabel("|$\Psi_6$|", fontsize=20)
ax1.text(4.2,0.85,"$\phi$: {:.3f}".format(mean_area_fraction)+"$+/-${:.3f}".format(std_area_frac),fontsize=18)

#ax1.plot(mean_acc[LOWER_BOUND:UPPER_BOUND], quintic(mean_acc[LOWER_BOUND:UPPER_BOUND], *popt), "r-")  #plot fit to data
print("midpoint of order: ", midpoint_order)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()