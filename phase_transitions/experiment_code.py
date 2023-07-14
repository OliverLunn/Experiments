import numpy as np
import time
from tqdm import tqdm
from shaker import shaker

shaker_obj = shaker.Shaker()
shaker_obj

duties = np.arange(670, 550, -2)


d0 = 680


for duty in tqdm(duties):
    shaker_obj.ramp(d0, duty, 0.5, -1)
    time.sleep(3)
    shaker_obj.set_duty_and_record(duty)
    time.sleep(15)
    shaker_obj.set_duty_and_record(duty)
    time.sleep(3)
    d0 = duty