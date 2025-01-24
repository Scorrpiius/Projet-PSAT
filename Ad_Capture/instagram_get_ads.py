import os
import random
import time
from datetime import datetime

import easyocr  # requires 'pip install easyocr'

import adb_utils as utils


def take_screenshot(filename="screenshot.png"):
    # Save screenshots in the "img" folder within the script's directory
    local_path = os.path.join(utils.instagram_folder, filename)

    os.system(f"adb shell screencap -p /sdcard/{filename}") # Take screenshot
    os.system(f"adb pull /sdcard/{filename} {local_path}") # Move screenshot to the local system
    os.system(f"adb shell rm /sdcard/{filename}") # Remove it from the phone
    
    # Check if it is an ad
    isAd = checkSponsoredTextInImage(local_path)
    
    print(f"Ad detected ? {f'{utils.GREEN}V{utils.RESET}' if isAd else f'{utils.RED}X{utils.RESET}'}")
    if (isAd):
        print(f"Screenshot of ad '{filename}' saved successfully in '{local_path}'")
    else:
        # Remove the screenshot if it is not an ad
        os.remove(local_path)
        print(f"Screenshot '{filename}' discarded as it does not contain 'sponsored' text.")

def checkSponsoredTextInImage(filepath):
    results = utils.reader.readtext(filepath)
    
    for box in results:
        if (box[1] == "Sponsorise" or box[1] == "Sponsorisé"):
            print(f"{filepath} is sponsored!")
            return True
    return False

def goToReels():
    utils.tap(700, 1800) # 700 2200 for other big phones
    time.sleep(3.0) # wait a bit for it to load

def screenThenSwipe(n=1000):
    for i in range(0, n):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")
        take_screenshot(f"instagram-ad_{formatted_time}.png")
        print(f"[{utils.GREEN}{i+1}{utils.RESET}/{utils.GREEN}{n}{utils.RESET}] Screenshot analyzed successfully! {utils.GREEN}V{utils.RESET}")
        noise = random.randint(3, 20)
        time.sleep(noise/10)
        utils.swipe(540 + noise, 1000-noise, 540 + noise, 200-noise, 300 - 2*noise)

def main():
    # Open Instagram and go in the "Reels" category
    utils.open_instagram()
    goToReels()
    # Take a screenshot, swipe
    screenThenSwipe(500)

if __name__ == "__main__":
    main()
