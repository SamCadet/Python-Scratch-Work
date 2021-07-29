import pyautogui
import time

# p. 466-467

time.sleep(5)
pyautogui.click()   # Click to make the window active.
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)   # Move down.
    pyautogui.drag(-distance, 0, duration=0.2)  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # Move up.

'''

When you run this program, there will be a five-second delay ➊ for you to move the mouse cursor over
the drawing program’s window with the Pencil or Brush tool selected. Then spiralDraw.py will take control
of the mouse and click to make the drawing program’s window active ➋. The active window is the window
that currently accepts keyboard input, and the actions you take—like typing or, in this case, dragging the
mouse—will affect that window. The active window is also known as the focused or foreground window. Once
the drawing program is active, spiralDraw.py draws a square spiral pattern like the one on the left of Figure
20-2. While you can also create a square spiral image by using the Pillow module discussed in Chapter 19,
creating the image by controlling the mouse to draw it in MS Paint lets you make use of this program’s
various brush styles, like in Figure 20-2 on the right, as well as other advanced features, like gradients or the
fill bucket. You can preselect the brush settings yourself (or have your Python code select these settings) and
then run the spiral-drawing program.

The distance variable starts at 200, so on the first iteration of the while loop, the first drag() call drags the
cursor 200 pixels to the right, taking 0.2 seconds ➌. distance is then decreased to 195 ➍, and the second drag()
call drags the cursor 195 pixels down ➎. The third drag() call drags the cursor –195 horizontally (195 to the
left) ➏, distance is decreased to 190, and the last drag() call drags the cursor 190 pixels up. On each iteration,
the mouse is dragged right, down, left, and up, and distance is slightly smaller than it was in the previous
iteration. By looping over this code, you can move the mouse cursor to draw a square spiral.
You could draw this spiral by hand (or rather, by mouse), but you’d have to work slowly to be so precise.
PyAutoGUI can do it in a few seconds!
'''
