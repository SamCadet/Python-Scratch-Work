#! python3

# prettifiedStopwatch.py - A new stopwatch, BOI!

import time
import pyperclip

# Display the program's instructions.
print('''Press ENTER to begin. Afterward, press ENTER
to "click" the stopwatch. Press Ctrl-C to quit.''')
input()                     # press Enter to begin
print('Started.')
startTime = time.time()     # get the first lap's start time
copy = ''  # assistance from answer here - https://github.com/kudeh/automate-the-boring-stuff-projects/blob/master/prettified-stopwatch/stopwatch.py
lastTime = startTime
lapNum = 1

# Start tracking the lap times.

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        board = 'Lap # %s: %s (%s)' % (
            str(lapNum), str(totalTime).center(7), str(lapTime).rjust(7))
        copy += board + '\n'
        print(board, end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
        pyperclip.copy(board)
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
