from tkinter import *

from keyboard import Keyboard

def press(key):
	print(key)

root = Tk()
root.title("Keyboard Module Self-Test")
kbd = Keyboard(root, press)
kbd.grid()
root.mainloop()