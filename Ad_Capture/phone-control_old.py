import os
import time

import easyocr  # requires 'pip install easyocr'

# Get the path of the folder where the script file is located
script_dir = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(script_dir, "img")

# Initialize the image reader
reader = easyocr.Reader(['fr']) 

def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")
    time.sleep(0.5)

def swipe(x1, y1, x2, y2, duration=1000):
    os.system(f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}")
    time.sleep(0.5)

def take_screenshot(filename="screenshot.png"):
    # Save screenshots in the "img" folder within the script's directory
    local_path = os.path.join(folder, filename)

    os.system(f"adb shell screencap -p /sdcard/{filename}") # Take screenshot
    os.system(f"adb pull /sdcard/{filename} {local_path}") # Move screenshot to the local system
    os.system(f"adb shell rm /sdcard/{filename}") # Remove it from the phone
    
    # Check if it is an ad
    isAd = checkSponsoredTextInImage(local_path)
    
    print(f"AD ? {isAd}")
    if (isAd):
        print(f"Screenshot of ad '{filename}' saved successfully in '{local_path}'")
    else:
        # Remove the screenshot if it is not an ad
        os.remove(local_path)
        print(f"Screenshot '{filename}' discarded as it does not contain 'sponsored' text.")

def checkSponsoredTextInImage(filepath):
    results = reader.readtext(filepath)
    
    for box in results:
        if (box[1] == "Sponsorise" or box[1] == "Sponsorisé"):
            print(f"{filepath} is sponsored!")
            return True
    return False

def open_instagram():
    os.system("adb shell monkey -p com.instagram.android -c android.intent.category.LAUNCHER 1")
    time.sleep(2.0)

# Open Instagram and go in the "Reels" category
open_instagram()
tap(700, 2200)
time.sleep(2.0) # wait a bit for it to load

# Take a screenshot, swipe
for i in range(10):
    take_screenshot(f"screenshot-instagram-{i}.png")
    swipe(540, 1000, 540, 800, 300)
