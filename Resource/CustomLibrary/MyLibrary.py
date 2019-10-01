
import string
from random import *
#import keyboard
from pynput.keyboard import Key, Controller

#########Keyword Emulation######################################

def cus_mouse_click_left(rptname):
    print("Click Image Coordinates")
    mouse = Controller()
    #mouse.position = (0, 300)
    #mouse.scroll(200, 300)
    mouse.press(Button.left)
    mouse.release(Button.left)

def cus_mouse_click_right(rptname):
    print("Click Image Coordinates")
    mouse = Controller()
    mouse.position = (500, 640)
    #mouse.scroll(200, 300)
    mouse.press(Button.right)
    mouse.release(Button.right)

def cus_mouse_move_position(rptname):
    print("Click Text Coordinates")
    mouse = Controller()
    mouse.position = (500, 640)
    mouse.press(Button.right)
    #mouse.move(500, 0)
    mouse.release(Button.right)

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

# Double click; this is different from pressing and releasing
# twice on Mac OSX

def cus_mouse_doubleclick():
    mouse.click(Button.left, 2)

# def double_click(self, event):
#     '''  set flag when there is a double click '''
#     self.double_click_flag = True
