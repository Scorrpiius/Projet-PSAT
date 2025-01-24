import os
import time
from datetime import datetime

import easyocr  # requires 'pip install easyocr'
from PIL import Image

import adb_utils as utils


def take_and_crop_screenshot(filename="compass-screenshot.png", crop_area=None):
    local_path = os.path.join(utils.compass_folder, filename)

    os.system(f"adb shell screencap -p /sdcard/{filename}") # Take screenshot
    os.system(f"adb pull /sdcard/{filename} {local_path}") # Move screenshot to the local system
    os.system(f"adb shell rm /sdcard/{filename}") # Remove it from the phone
    
    # If a crop area is specified, crop the image
    if crop_area:
        with Image.open(local_path) as img:
            cropped_img = img.crop(crop_area)  # Crop the image
            cropped_img.save(local_path)  # Overwrite the original file
            print(f"Screenshot cropped and saved at {local_path}")
    else:
        print(f"Screenshot saved at {local_path}")

def get_ad():
    # Take a first screenshot of ad
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    take_and_crop_screenshot(f"compass_first_ad_{formatted_time}.png")

    # Skip the first ad
    time.sleep(7.0)
    utils.tap(900, 100) # tap top right corner
    time.sleep(2.5)

    # Take a second cropped screenshot inside the app
    utils.tap(1000, 1100) # minimize ad / (1000, 1460 for other big phones
    crop_area = (0, 1720, 1080, 1920) # (0, 2200, 1080, 2400) for other big phones
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    take_and_crop_screenshot(f"compass_second_ad_{formatted_time}.png", crop_area)

def main():
    # Open compass app
    utils.open_compass()
    time.sleep(5.0) # wait loading
    get_ad()
    
if __name__ == "__main__":
    main()

