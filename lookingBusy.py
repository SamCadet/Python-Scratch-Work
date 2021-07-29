#! python3
'''

lookingBusy.py - just a little something for the cars that be bumpin'

'''

import pyautogui
import time


# Establish positions for mouse, making variables makes it easy to change values later

position1 = (2039, 1162)
position2 = (2137, 1104)

# Warn the user about the program starting

# Make a value to break the loop later

timeout = time.time() + 60 * 1  # One minute from now

# Move mouse every 10 seconds in a loop

print('>>> This thang\'s about to start in 5 seconds so make sure the desktop\'s where you want it! Press CTRL-C To stop the program now...<<<')
time.sleep(5)

while True:

    # move mouse to position1
    pyautogui.moveTo(position1[0], position1[1], duration=0.25)
    # pauses program for 10 seconds
    pyautogui.sleep(10)
    # move mouse to position2
    pyautogui.moveTo(position2[0], position2[1], duration=0.25)
    # another pause
    pyautogui.sleep(10)
    # break the loop so it doesn't run forever
    if time.time() > timeout:
        break
