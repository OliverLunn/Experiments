import numpy as np
import time
from tqdm import tqdm
from shaker import Shaker


shaker = Shaker()

duties = np.arange(560, 400, -5)
duty_0 = 550

for duty in tqdm(duties):
    shaker.ramp(duty_0, duty, 0.5)
    time.sleep(5)
    shaker.set_duty_and_record(duty)
    time.sleep(15)
    shaker.set_duty_and_record(duty)
    time.sleep(5)
    duty_0 = duty
    
