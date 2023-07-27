import numpy as np
import time
import serial
from tqdm import tqdm
from shaker import shaker

def pk_acceleration(object):
    """
    This function reads data from RPi Pico accelerometer and outputs current
    peak z-acceleration reading.

    ----Input: ----
    Object: Reads data from RPi Pico

    ----Returns: ----
    peak_z [float] : Peak accleration measured. (Γ)
    
    """
    line = object.readline()
    if line:
        string = line.decode()
        string = string.split(',')
        peak_z = float(string[-1])
    
    return peak_z


shaker_obj = shaker.Shaker()    #create shaker object
acc_obj = serial.Serial('COM8', 9600, timeout=None) #create accelerometer object

duties = np.arange(700, 570, -5)    #create arrays of duty values
acc = [] 
acc1 = []   #empty array for acc data
d0 = 710   #initial duty values
duties1 = np.arange(570,700, 5)    #create arrays of duty values
d01 = 568

for duty in tqdm(duties):   #perform experiment
    shaker_obj.ramp(d0, duty, 0.25, -1)
    shaker_obj.set_duty(duty)
    time.sleep(15)
    acceleration = pk_acceleration(acc_obj)
    acc.append(acceleration)
    shaker_obj.set_duty_and_record(duty)
    time.sleep(3)
    shaker_obj.set_duty_and_record(duty)
    time.sleep(3)
    d0 = duty

for duty1 in tqdm(duties1):   #perform experiment
    shaker_obj.ramp(d01, duty1, 0.25, 1)
    shaker_obj.set_duty(duty1)
    time.sleep(15)
    acceleration = pk_acceleration(acc_obj)
    acc1.append(acceleration)
    shaker_obj.set_duty_and_record(duty1)
    time.sleep(3)
    shaker_obj.set_duty_and_record(duty1)
    time.sleep(3)
    d01 = duty1

np.savetxt("acceleration_data_2c.txt", acc, delimiter=",")
np.savetxt("acceleration_data_2h.txt", acc1, delimiter=",")