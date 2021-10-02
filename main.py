import os
import time

try:
    import pyautogui
except ImportError:
    os.system("pip3 install pyautogui")
    import pyautogui

fileName = input("Please enter the name of the txt file you would like to open: ")
interval = input("Please enter the interval of each message: ")

if len(interval) < 1:
    interval = 0
else:
    interval = int(interval)

file = open(fileName, "r")

print("Starting the spam in 5 seconds...")
time.sleep(1)
print("Starting the spam in 4 seconds...")
time.sleep(1)
print("Starting the spam in 3 seconds...")
time.sleep(1)
print("Starting the spam in 2 seconds...")
time.sleep(1)
print("Starting the spam in 1 seconds...")
time.sleep(1)

for line in file:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    time.sleep(interval)