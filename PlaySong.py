from tkinter import *

x=Tk()


def fxn():
	import os
	os.system('start C:\music') #select folder
	os.system('start Luis.mp3') #select song
	


y=Button(x,text="Do you want listen song",command=fxn)
y.pack()

x.mainloop()

