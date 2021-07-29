#! python3
# countdown.py - A simple countdown script.

import time
import subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.

subprocess.Popen('40. 9th Wonder - CountemUp!!!!.mp3', shell=True)
