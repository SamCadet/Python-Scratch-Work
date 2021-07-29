#! python3

# copyTextField - automate copying text

import pyperclip
import pyautogui


# Bring text editor to the front with pyautogui


np = pyautogui.getActiveWindow()
np.activate()

# np = pyautogui.getWindowsWithTitle('Notepad')

# pyautogui.getActiveWindow()

# np.activate()

# Click on text editor and copy everything in it

space = (1422, 941)

pyautogui.click(space[0], space[1], duration=0.25)
# pyautogui.click()
pyautogui.hotkey('ctrl', 'a', duration=0.25)
pyautogui.hotkey('ctrl', 'c', duration=0.25)

# Paste the text from pyperclip

message = pyperclip.paste()
print(message)
