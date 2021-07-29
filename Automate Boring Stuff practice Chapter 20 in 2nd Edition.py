import pyautogui
import time

'''
# p. 463-464

Controlling Mouse Movement

The mouse functions of PyAutoGUI use x- and y-coordinates. Figure 20-1 shows the
coordinate system for the computer screen; it’s similar to the coordinate system
used for images, discussed in Chapter 19. The origin, where x and y are both
zero, is at the upper-left corner of the screen.

The pyautogui.size() function returns a two-integer tuple of the screen’s
width and height in pixels.

wh = pyautogui.size()  # Obtain the screen resolution
print(wh)
print(wh[0])
print(wh.width)  # these are interchangeable to return the width of the screen

# p. 464-465 Moving the Mouse


The pyautogui.moveTo() function will instantly move the mouse cursor to a
specified position on the screen. Integer values for the x- and ycoordinates
make up the function’s first and second arguments, respectively. An optional
duration integer or float keyword argument specifies the number of seconds it
should take to move the mouse to the destination. If you leave it out, the default is 0 for instantaneous movement. (All of the duration keyword arguments in
PyAutoGUI functions are optional.)



for i in range(10):  # Move the mouse in a square.)
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)


This example moves the mouse cursor clockwise in a square pattern among the four
coordinates provided a total of 10 times. Each movement takes a quarter of a
second, as specified by the duration = 0.25 keyword argument. If you hadn’t passed a
third argument to any of the pyautogui.moveTo() calls, the mouse cursor would
have instantly teleported from point to point.

The pyautogui.move() function moves the mouse cursor relative to its current position. The following example
moves the mouse in the same square pattern, except it begins the square from wherever the mouse happens
to be on the screen when the code starts running:



for i in range(10):
    pyautogui.move(100, 0, duration=0.25)   # right
    pyautogui.move(0, 100, duration=0.25)   # down
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up

The pyautogui.move() function also takes three arguments: how many pixels to move
horizontally to the right, how many pixels to move vertically downward, and
(optionally) how long it should take to complete the movement. A negative integer
for the first or second argument will cause the mouse to move left or
upward, respectively.



# p. 465 Getting the Mouse Position

You can determine the mouse’s current position by calling the pyautogui.position() function,
which will return a Point named tuple of the mouse cursor’s x and y positions
at the time of the function call.


print(pyautogui.position())     # Get the current mouse position
print(pyautogui.position())     # Get current mouse position again
p = pyautogui.position()        # and again
print(p)

print(p[0])     # The x-coordinate is at index 0.
print(p.x)      # The x-coordinate is also in the x attribute.


# p. 465-466 Clicking the Mouse

To send a virtual mouse click to your computer, call the pyautogui.click() method.
By default, this click uses the left mouse button and takes place wherever the
mouse cursor is currently located.

You can pass x- and y-coordinates of the click as optional first and second
arguments if you want it to take place somewhere other than the mouse’s
current position.

If you want to specify which mouse button to use, include the button keyword
argument, with a value of 'left', 'middle', or 'right'. For example,
pyautogui.click(100, 150, button='left') will click the left mouse button at
the coordinates (100, 150), while pyautogui.click(200, 250, button='right')
will perform a right-click at (200, 250).

pyautogui.click(10, 5)  # Move mouse to (10, 5) and click.

A full “click” is defined as pushing a mouse button down and then releasing it
back up without moving the cursor. You can also perform a click by calling
pyautogui.mouseDown(), which only pushes the mouse button down, and
pyautogui.mouseUp(), which only releases the button. These functions have the
same arguments as click(), andin fact, the click() function is just a
convenient wrapper around these two function calls.

As a further convenience, the pyautogui.doubleClick() function will perform two
clicks with the left mouse button, while the pyautogui.rightClick() and
pyautogui.middleClick() functions will perform a click with the right and
middle mouse buttons, respectively.

PyAutoGUI provides the pyautogui.dragTo() and pyautogui.drag() functions to drag
the mouse cursor to a new location or a location relative to its current one.
The arguments for dragTo() and drag() are the same as moveTo() and move():
the x-coordinate/horizontal movement, the y-coordinate/vertical movement, and an
optional duration of time. (macOS does not drag correctly when the mouse moves too
quickly, so passing a duration keyword argument is recommended.)

# p. 467 Scrolling the Mouse

The final PyAutoGUI mouse function is scroll(), which you pass an integer
argument for how many units you want to scroll the mouse up or down.

Passing a positive integer scrolls up, and passing a negative integer
scrolls down.


pyautogui.scroll(200)

You’ll see Mu scroll upward if the mouse cursor is over a text field
that can be scrolled up.

# p. 468 Planning Your Mouse Movements

The pyautogui.mouseInfo() function is meant to be called from the
interactive shell, rather than as part of your program. It launches
a small application named MouseInfo that’s included with PyAutoGUI.


pyautogui.mouseInfo()

This makes the MouseInfo window appear. This window gives you information
about the mouse’s cursor current position, as well the color of the
pixel underneath the mouse cursor, as a three-integer RGB tuple
and as a hex value.

By default, the 3 Sec. Button Delay checkbox is checked, causing a
three-second delay between clicking a Copy or Log button and the copying
or logging taking place. This gives you a short amount of time in
which to click the button and then move the mouse into your desired
position. It may be easier to uncheck this box, move the mouse into
position, and press the F1 to F8 keys to copy or log the mouse position.
You can look at the Copy and Log menus at the top of the MouseInfo
window to find out which key maps to which buttons.

For example, uncheck the 3 Sec. Button Delay, then move the mouse around
the screen while pressing the F6 button, and notice how the x- and
y-coordinates of the mouse are recorded in the large text field in
the middle of the window. You can later use these coordinates in
your PyAutoGUI scripts.

# p. 469 Getting a Screenshot

To take screenshots in Python, call the pyautogui.screenshot() function.


im = pyautogui.screenshot()

The im variable will contain the Image object of the screenshot.
You can now call methods on the Image object in the im variable,
just like any other Image object.

# Analyzing the Screenshot

You can obtain the RGB color value of a particular pixel on the
screen with the .getpixel() method.


im = pyautogui.screenshot()

# updated documentation here https://pyautogui.readthedocs.io/en/latest/screenshot.html
print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))



PyAutoGUI’s pixelMatchesColor() function will return True
if the pixel at the given x - and y - coordinates on the screen
matches the given color. The first and second arguments are
integers for the x - and y - coordinates, and the third argument
is a tuple of three integers for the RGB color the screen pixel
must match.


pyautogui.pixel((50, 200))
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))

# p. 470 Image Recognition

If you have previously taken a screenshot to capture
the image of a Submit button in submit.png, the locateOnScreen()
function will return the coordinates where that image is found.

b = pyautogui.locateOnScreen('screenshot.png')
print(b)
print(b[0])
print(b.left)



print(list(pyautogui.locateAllOnScreen('screenshot.png')))

Once you have the four-integer tuple for the specific image you
want to select, you can click the center of this area by passing
the tuple to click(). Enter the following into the interactive shell:

>>> pyautogui.click((643, 745, 70, 29))

As a shortcut, you can also pass the image filename directly to the
click() function:

>>> pyautogui.click('submit.png')

The moveTo() and dragTo() functions also accept image filename arguments.
Remember locateOnScreen() raises an exception if it can’t find the image
on the screen, so you should call it from inside a try statement:

try:
    location = pyautogui.locateOnScreen('submit.png')
except:
    print('Image could not be found.')

Without the try and except statements, the uncaught exception would crash
your program. Since you can’t be sure that your program will always find
the image, it’s a good idea to use the try and except statements
when calling locateOnScreen().

# p. 471 Obtaining the Active Window

If you need to find where a particular window is on the
screen, it’s faster and more reliable to use PyAutoGUI’s window features.



fw = pyautogui.getActiveWindow()
fw
str(fw)
fw.title
fw.size
fw.left, fw.top, fw.right, fw.bottom
fw.topleft
fw.area
pyautogui.click(fw.left + 10, fw.top + 20)

You can now use these attributes to calculate precise coordinates within a
window. If you know that a button you want to click is always 10 pixels
to the right of and 20 pixels down from the window’s top-left corner,
and the window’s top-left corner is at screen coordinates (300, 500),
then calling pyautogui.click(310,520)
(or pyautogui.click(fw.left + 10, fw.top + 20) if fw contains the
Window object for the window) will click the button. This way, you
won’t have to rely on the slower, less reliable locateOnScreen()
function to find the button for you.

Other Ways of Obtaining Windows

pyautogui.getAllWindows() Returns a list of Window objects for every visible window on the screen.

pyautogui.getWindowsAt(x, y) Returns a list of Window objects for every visible window that includes the point
(x, y).

pyautogui.getWindowsWithTitle(title) Returns a list of Window objects for every visible window that includes
the string title in its title bar.

pyautogui.getActiveWindow() Returns the Window object for the window that is currently receiving keyboard
focus.

Manipulating Windows

Windows attributes can do more than just tell you the size and position of the window. You can also set their
values in order to resize or move the window.



fw = pyautogui.getActiveWindow()
print(fw.width)     # Gets the current width of the window
print(fw.topleft)   # Gets the current position of the window.
fw.width = 1000     # Resizes the width.
fw.topleft = (800, 400)     # Moves the window.




fw = pyautogui.getActiveWindow()
print(fw.isMaximized)  # Returns True if window is maximized
print(fw.isMinimized)  # Returns True if window is minimized
print(fw.isActive)     # Returns True if window is the active window.
fw.maximize()           # Maximizes the window.
print(fw.isMaximized)
fw.restore()            # undoes a minimize/maximize action.
# Wait 5 seconds while you active a different window.
time.sleep(5)
fw.activate()
fw.close()              # This will close the window you're typing in.

The close() method will close a window. Be careful with this method, as it may bypass any message
dialogs asking you to save your work before quitting the application.


pyautogui.click(100, 200)
pyautogui.write('Ayo, #MyGuy!')

By default, the write() function will type the full string instantly. However, you can pass an optional
second argument to add a short pause between each character. This second argument is an integer or float
value of the number of seconds to pause. For example, pyautogui.write('Hello, world!', 0.25) will wait a
quarter-second after typing H, another quarter-second after e, and so on.

# p. 475 Key Names

Instead of a single string argument, a list of these keyboard key strings can be passed to write().


pyautogui.write(['a', 'b', 'left', 'left', 'x', 'y'])

# p. 476 Pressing and Releasing the Keyboard

Much like the mouseDown() and mouseUp() functions, pyautogui.keyDown() and pyautogui.keyUp() will send virtual
keypresses and releases to the computer.


pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

If you need to type a string into a text field, the write() function is
more suitable. But for applications that take single - key commands,
the press() function is the simpler approach.


# p. 476 Hotkey Combinations

# pyautogui.hotkey('ctrl', 'c')

# Use this instead of multiple lines with keyDown() and keyUp() to simplify code.

# p. 477 Setting Up Your GUI Automation Scripts


pyautogui.sleep(3)      # Pause the program for 3 seconds.
pyautogui.countdown(10)     # Counts down over 10 seconds.
print('Starting in ', end='')
pyautogui.countdown(3)

# p. 477-478 Review of the PyAutoGUI Functions

moveTo(x, y) Moves the mouse cursor to the given x and y coordinates.

move(xOffset, yOffset) Moves the mouse cursor relative to its current position.

dragTo(x, y) Moves the mouse cursor while the left button is held down.

drag(xOffset, yOffset) Moves the mouse cursor relative to its current position

click(x, y, button) Simulates a click (left button by default).

rightClick() Simulates a right-button click.

middleClick() Simulates a middle-button click.

doubleClick() Simulates a double left-button click.

mouseDown(x, y, button) Simulates pressing down the given button at the position x, y.

mouseUp(x, y, button) Simulates releasing the given button at the position x, y.

scroll(units) Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls
down.

write(message) Types the characters in the given message string.

write([key1, key2, key3]) Types the given keyboard key strings.

press(key) Presses the given keyboard key string.

keyDown(key) Simulates pressing down the given keyboard key.

keyUp(key) Simulates releasing the given keyboard key.

hotkey([key1, key2, key3]) Simulates pressing the given keyboard key strings down in order and then
releasing them in reverse order.

screenshot() Returns a screenshot as an Image object. (See Chapter 19 for information on Image objects.)

getActiveWindow(), getAllWindows(), getWindowsAt(), and getWindowsWithTitle() These functions return
Window objects that can resize and reposition application windows on the desktop.

getAllTitles() Returns a list of strings of the title bar text of every window on the desktop.

PyAutoGUI offers pop-up message boxes to provide notifications to the user and receive
input from them. There are four message box functions:

pyautogui.alert(text) Displays text and has a single OK button.

pyautogui.confirm(text) Displays text and has OK and Cancel buttons, returning either 'OK' or 'Cancel'
depending on the button clicked.

pyautogui.prompt(text) Displays text and has a text field for the user to type in, which it returns as a string.

pyautogui.password(text) Is the same as prompt(), but displays asterisks so the user can enter sensitive
information such as a password.

These functions also have an optional second parameter that accepts a string value to use as the title in
the title bar of the message box. The functions won’t return until the user has clicked a button on them, so
they can also be used to introduce pauses into your PyAutoGUI programs.
'''

pyautogui.alert('This is a message.', 'Important')
pyautogui.confirm('Do you want to continue?')  # Click Cancel
pyautogui.prompt('Do you love orange soda?')
pyautogui.password('What is the password?')
