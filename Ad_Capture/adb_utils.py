import os
import time

import easyocr  # requires 'pip install easyocr'

# ANSI codes
GREEN = '\033[32m'
CYAN = '\033[36m'
RED = '\033[31m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Get the path of the folder where the script file is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize all folders
instagram_folder = os.path.join(script_dir, "instagram-ads")
tiktok_folder = os.path.join(script_dir, "tiktok-ads")
compass_folder = os.path.join(script_dir, "compass-ads")
calculator_folder = os.path.join(script_dir, "calculator-ads")

# Initialize the image reader
reader = easyocr.Reader(['fr'])

# Adb functions
def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")
    time.sleep(0.5)

def swipe(x1, y1, x2, y2, duration=1000):
    os.system(f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}")
    time.sleep(0.5)
    
def open_instagram():
    os.system("adb shell monkey -p com.instagram.android -c android.intent.category.LAUNCHER 1")
    time.sleep(2.0)

def open_tiktok():
    os.system("adb shell monkey -p com.zhiliaoapp.musically -c android.intent.category.LAUNCHER 1")

def open_calculator():
    os.system("adb shell monkey -p com.dencreak.dlcalculator -c android.intent.category.LAUNCHER 1")
    time.sleep(2.0)
    
def open_compass():
    os.system("adb shell monkey -p compass.freecompassapp.digitalcompass -c android.intent.category.LAUNCHER 1")
    
def close_instagram():
    os.system("adb shell am force-stop com.instagram.android")
    time.sleep(2.0)
    
def close_tiktok():
    os.system("adb shell am force-stop com.zhiliaoapp.musically")
    time.sleep(2.0)

def close_compass():
    os.system("adb shell am force-stop compass.freecompassapp.digitalcompass")
    time.sleep(2.0)

def close_calculator():
    os.system("adb shell am force-stop com.dencreak.dlcalculator")
    time.sleep(2.0)
