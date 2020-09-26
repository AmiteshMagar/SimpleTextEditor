from tkinter import *
from tkinter.filedialog import *

filename = "Untitled"

def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)

def saveFile():
	global filename
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write (t)
	f.close()

def saveAs():
	f = asksaveasfile(mode = 'w', defaultextension = '.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror( title ="Error occured", message = " Unable to save file.")

def openFile():
	f = askopenfile(mode = 'r')
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)

root = Tk()
root.title("Simple Text Editor")
root.minsize(width = 400, height = 600)
root.maxsize(width = 400, height = 600)

text = Text(root, width = 400, height = 600)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = "New", command = newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command( label = "Save as", command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = "Quit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label = )
root.config(menu = menubar)
root.mainloop()