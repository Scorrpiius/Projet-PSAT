import os
import time
from datetime import datetime

import easyocr  # requires 'pip install easyocr'
from PIL import Image

import adb_utils as utils


def take_and_crop_screenshot(filename="calculator-screenshot.png", crop_area=None):
    local_path = os.path.join(utils.calculator_folder, filename)

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
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    crop_area = (0, 1670, 1080, 1820) # (0, 2100, 1080, 2300) for other big phones
    take_and_crop_screenshot(f"calculator_ad_{formatted_time}.png", crop_area)

def main():
    utils.open_calculator()
    time.sleep(5.0)
    get_ad()

if __name__ == "__main__":
    main()
