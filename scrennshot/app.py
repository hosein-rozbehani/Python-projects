"""screenshot""" 

import os 
import pyautogui

os.system(command="cls")

screenshot = pyautogui.screenshot()
screenshot.save("screenshot_01.png")

from PIL import ImageGrab

screenshot = ImageGrab.grab()
screenshot.save("screenshot._02.png")

from mss import mss

screenshot = mss()
screenshot.shot(mon=1)
