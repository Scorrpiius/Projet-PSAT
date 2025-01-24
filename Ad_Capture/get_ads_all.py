import os
import random
import time
from datetime import datetime

import adb_utils as utils
import calculator_get_ad as calculator
import compass_get_ad as compass
import instagram_get_ads as instagram
import tiktok_get_ads as tiktok

iteration = 1
while(True):
    noise = round(random.uniform(1,3), 3)
    print("=========================================")
    print(f"Iteration {utils.BOLD}{utils.CYAN}{iteration}{utils.RESET} started with noise={utils.BOLD}{utils.GREEN}{noise}{utils.RESET} !")
    utils.open_tiktok()
    time.sleep(2.0 + noise)
    tiktok.screenThenSwipe(15)
    utils.close_tiktok()
    
    utils.open_instagram()
    instagram.goToReels()
    instagram.screenThenSwipe(15)
    utils.close_instagram()
    
    utils.open_compass()
    time.sleep(5.0 + noise) # wait loading
    compass.get_ad()
    utils.close_compass()

    utils.open_calculator()
    time.sleep(5.0 + noise)
    calculator.get_ad()
    utils.close_calculator()
    
    time.sleep(1.0 + noise)
    iteration += 1