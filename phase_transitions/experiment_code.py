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


duties = np.arange(700, 580, -2)    #create arrays of duty values
acc = []    #empty array for acc data
d0 = 720    #initial duty values

for duty in tqdm(duties):   #perform experiment
    shaker_obj.ramp(d0, duty, 1, -1)
    time.sleep(2)
    shaker_obj.set_duty(duty)
    time.sleep(5)
    shaker_obj.set_duty_and_record(duty)
    acceleration = pk_acceleration(acc_obj)
    acc.append(acceleration)
    time.sleep(3)
    shaker_obj.set_duty_and_record(duty)
    time.sleep(3)
    d0 = duty

np.savetxt("acceleration_data_1.txt", acc, delimiter=",")
