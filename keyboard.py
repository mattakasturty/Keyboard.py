from layout import *
from tkinter import *

class Keyboard(Frame):
	def __init__(self, parent, callback):
		Frame.__init__(self, parent)
		self.grid()
		self.state = "Normal"
		for i in range(0, 5, 1):
			c = 0
			for n in range(0, len(layout[i]), 1):
				b = Button(parent, text = layout[i][n][0], command = lambda name=layout[i][n][0]: self.press(callback,name))

				b.grid(row = i, column = c, columnspan = layout[i][n][-1], sticky = N+S+E+W)
				c += layout[i][n][1]

	def press(self,callback, name):
		if(name.isalpha() and len(name) == 1):
			if(self.state == "Normal"):
				name = name.lower()
			callback(name)
			if(self.state == "Shifted"):
				self.state = "Normal"
		elif(name == "Shift"):
			if(self.state == "Shifted" or self.state == "Caps"):
				self.state = "Normal"
			else:
				self.state = "Shifted"
		elif(name == "CapsLock"):
			if(self.state == "Caps"):
				self.state = "Normal"
			else:
				self.state = "Caps"
		elif(name in ["Tab", "Ctrl", "Alt", "Space", "Enter", "Backspace"]):
			callback(name)
		else:
			if(self.state == "Shifted"):
				callback(name[0])
				self.state = "Normal"
			else:
				callback(name[-1])