from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Simple Text Editor')
root.geometry ("1200x660")

#Checking existance of a saved file
global filename_token 
filename_token = False

#create newFile function
def NewFile():
	frame_text.delete(1.0, END)
	root.title("New file")
	status_bar.config(text = "New file")
	global filename_token
	filename_token=False

#create openFile function
def OpenFile():
	text_file = filedialog.askopenfilename(initialdir="~/homme/darthamitesh/",title = "Open file", filetypes=(("Text files", "*.txt"),("Python files", "*.py"),("HTML files", "*.html"),("All files", "*.*")))
	#Check filename
	if text_file:
		global filename_token 
		filename_token = text_file
	frame_text.delete(1.0, END)
	filename = text_file
	filename = filename.replace("~/home/darthamitesh/","")
	status_bar.config(text = f"{filename}")
	root.title(f"{filename}")
	#fetch file
	text_file = open(text_file, 'r')
	tempVar = text_file.read()
	frame_text.insert(END, tempVar)
	text_file.close()

#Create save as function
def SaveFileAs():
	text_file = filedialog.asksaveasfilename(initialdir="~/home/darthamitesh/",defaultextension = ".txt", title = "Save file as", filetypes =(("Text files","*.txt"), ("HTML files", "*.html"), ("Python files", "*.py"), ("All files", "*.*")))
	if text_file:
		filename = text_file
		filename = filename.replace("~/home/darthamitesh/","")
		root.title(f"{filename}")
		status_bar.config(text = f"Saved : {filename}")
		#saving
		text_file = open(text_file, 'w')
		text_file.write(frame_text.get(1.0,END))
		text_file.close()
		save_notif = Toplevel()
		save_notif.title("Save Notification")
		global save_lbl
		save_lbl = Label(save_notif, text = "All changes have been saved.")
		save_lbl.pack()
		#pop up box notification


#Create Save function
def SaveFile():
	global filename_token 
	#in case the file has a name assigned
	if filename_token:
		#saving
		text_file = open(filename_token, 'w')
		text_file.write(frame_text.get(1.0,END))
		text_file.close()
		save_notif = Toplevel()
		save_notif.title("Save Notification")
		global save_lbl
		save_lbl = Label(save_notif, text = "All changes have been saved.", pady = 30, padx = 30)
		save_lbl.pack()
		status_bar.config(text = f"Saved : {filename_token}")
	#in case the file was never saved before
	else:
		SaveFileAs()


#Create main frame
primary_frame = Frame(root)
primary_frame.pack(pady = 5)

#Create Scroll bar for the text box
text_scroll = Scrollbar(primary_frame)
text_scroll.pack(side = RIGHT, fill = Y)

#Create a text box
frame_text = Text(primary_frame, width = 97, height = 25, font = ("Helvetica", 16), selectbackground = "cyan", selectforeground = "black", undo=True, yscrollcommand = text_scroll.set)
frame_text.pack()

#Create menu
menubar = Menu(root)
root.config(menu=menubar)

#add File Menu
file_menu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = NewFile)
file_menu.add_command(label = "Open", command = OpenFile)
file_menu.add_command(label = "Save", command = SaveFile)
file_menu.add_command(label = "Save As", command = SaveFileAs)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

#add Edit Menu
edit_menu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Copy")
edit_menu.add_command(label = "Paste")
edit_menu.add_command(label = "Undo")
edit_menu.add_command(label = "Redo")

#add Status bar to text pane 
status_bar = Label(root, text = "Ready  ", anchor = W)
status_bar.pack(fill=X, side=BOTTOM, ipady = 5)

text_scroll.config(command = frame_text.yview)

root.mainloop()