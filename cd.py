from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
# Importing some Windows libraries. To use them type pip install pywin32 in console.
desk = GetDC(0) # Get the first monitor and store it in our desk variable
x = GetSystemMetrics(0) # Get screen width and store it in x
y = GetSystemMetrics(1) # Get screen height and store it in y
# Let's try changing its color! We can do that using SelectObject and CreateSolidBrush!
for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        255, # Red value
        0, # Green value
        0 # Blue value
    )) # Creates a brush
    SelectObject(desk, brush) # Choose that we're drawing with our brush.
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # Frees up memory. Pretty necessary to avoid crashes etc.
    Sleep(10) # Waits 10 milliseconds
