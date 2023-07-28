import numpy as np
import time
from tqdm import tqdm
from shaker.shaker import Shaker
from labequipment.arduino import Arduino
from shaker.settings import accelerometer_shaker

def pk_acceleration(ard):
    """
    This function reads data from RPi Pico accelerometer and outputs current
    peak z-acceleration reading.

    ----Input: ----
    Object: Reads data from RPi Pico

    ----Returns: ----
    peak_z [float] : Peak accleration measured. (Γ)
    
    """
    ard.flush()
    line = ard.read_serial_line()
    data_vals = line.split(',')
    peak_z = float(data_vals[-1])
    return peak_z

if __name__ == '__main__':

    with Shaker() as shaker_obj, Arduino(accelerometer_shaker) as acc_obj:
    
        duties = np.arange(700, 570, -5)    #create arrays of duty values
        duties1 = np.arange(570, 700, 5)
        acc = []
        acc1 = [] 
        d0 = 702   #initial duty values
        d1 = 568

        for duty in tqdm(duties):   #perform experiment (cooling cycle)
            shaker_obj.ramp(d0, duty, 2, -1) 
            shaker_obj.set_duty(duty)
            time.sleep(8)
            acceleration = pk_acceleration(acc_obj)
            acc.append(acceleration) 
            shaker_obj.set_duty_and_record(duty)
            time.sleep(3)
            shaker_obj.set_duty_and_record(duty)
            time.sleep(2)
            d0 = duty

        for duty1 in tqdm(duties1):   #perform experiment (heating cycle)
            shaker_obj.ramp(d1, duty1, 2, 1) 
            shaker_obj.set_duty(duty1)
            time.sleep(8)
            acceleration = pk_acceleration(acc_obj)
            acc1.append(acceleration) 
            shaker_obj.set_duty_and_record(duty1)
            time.sleep(3)
            shaker_obj.set_duty_and_record(duty1)
            time.sleep(2)
            d1 = duty1

    np.savetxt("acceleration_data_1c.txt", acc, delimiter=",")
    np.savetxt("acceleration_data_1h.txt", acc1, delimiter=",")