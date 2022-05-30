a=input("Enter the text:")
b=int(input("How many its want to type:"))
from pynput.keyboard import Key,Controller
import time
def keyboardController():
    keyboard = Controller()
    time.sleep(3)
    for i in range(0,b):
        keyboard.type(a)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
keyboardController()
