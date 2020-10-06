from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Simple Text Editor')
root.geometry ("1200x680")

#Checking existance of a saved file
global filename_token 
filename_token = False

global selected_text
selected_text = False

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

#Function for 'cutting' a piece of text
def CutText(argu):
	global selected_text

	if argu:
		selected_text = root.clipboard_get()
	else:
		if (frame_text.selection_get()):
			#Get selected text
			selected_text = frame_text.selection_get()
			#delete selected text
			frame_text.delete("sel.first", "sel.last")
			#clear clipboard and append
			root.clipboard_clear()
			root.clipboard_append(selected_text)


#Function for copying text
def CopyText(argu):
	global selected_text
	#check if shortcut was used
	if argu:
		selected_text = root.clipboard_get()
	else:	
		if(frame_text.selection_get()):
			selected_text = frame_text.selection_get()
			root.clipboard_clear()
			root.clipboard_append(selected_text)

#Function for pasting text
def PasteText(argu):
	global selected_text
	if argu:
		selected_text = root.clipboard_get()
	else:
		if(selected_text):
			cursor_posn = frame_text.index(INSERT)
			frame_text.insert(cursor_posn, selected_text)

def SelectAll(argu):
	if(argu):
		frame_text.tag_add('sel', '1.0', 'end')

#function to write bold text
def to_bold():
	global selected_text
	Bold_font = font.Font(frame_text, frame_text.cget("font"))
	Bold_font.configure(weight = "bold")

	#configure a tag
	frame_text.tag_configure("bold", font = Bold_font)

	#defining current tags
	current_tags = frame_text.tag_names("sel.first")

	#see if tag has been set
	if "bold" in current_tags:
		frame_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		frame_text.tag_add("bold", "sel.first", "sel.last")
#function to write italic text
def to_ital():
	global selected_text
	Italics_font = font.Font(frame_text, frame_text.cget("font"))
	Italics_font.configure(slant = "italic")

	#configure a tag
	frame_text.tag_configure("italic", font = Italics_font)

	#defining current tags
	current_tags = frame_text.tag_names("sel.first")

	#see if tag has been set
	if "italic" in current_tags:
		frame_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		frame_text.tag_add("italic", "sel.first", "sel.last")

#toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)

#Create main frame
primary_frame = Frame(root)
primary_frame.pack(pady = 5)

#Create Scroll bar for the text box
verti_scroll = Scrollbar(primary_frame)
verti_scroll.pack(side = RIGHT, fill = Y)

#Horizontal scroll bar
horiz_scroll = Scrollbar(primary_frame, orient='horizontal')
horiz_scroll.pack(side = BOTTOM, fill = X)

#Create a text box
frame_text = Text(primary_frame, width = 97, height = 25, font = ("Helvetica", 16), selectbackground = "cyan", selectforeground = "black", undo=True, xscrollcommand=horiz_scroll.set,yscrollcommand = verti_scroll.set, wrap="none")
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
edit_menu.add_command(label = "Cut", command = lambda: CutText(False), accelerator="Ctrl+x")
edit_menu.add_command(label = "Copy", command = lambda: CopyText(False), accelerator="Ctrl+c")
edit_menu.add_command(label = "Paste    ", command = lambda: PasteText(False), accelerator="Ctrl+v")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = frame_text.edit_undo, accelerator="Ctrl+z")
edit_menu.add_command(label = "Redo    ", command = frame_text.edit_redo, accelerator="Ctrl+Shift+z")

#add Status bar to text pane 
status_bar = Label(root, text = "Ready  ", anchor = W)
status_bar.pack(fill=X, side=BOTTOM, ipady = 8)

verti_scroll.config(command = frame_text.yview)
horiz_scroll.config(command = frame_text.xview)

#Edit bindings
root.bind('<Control-Key-x>', CutText)
root.bind('<Control-Key-c>', CopyText)
root.bind('<Control-Key-v>', PasteText)
root.bind('<Control-Key-a>', SelectAll)
 

#Bold Button
button_bold = Button(toolbar_frame, text = "Bold", command = to_bold)
button_bold.grid(row =0, column = 0, sticky = W, padx = 5)

#Italic Button
button_italics = Button(toolbar_frame, text = "Italics", command = to_ital)
button_italics.grid(row =0, column = 1, padx = 5)

#root.clipboard_append(" ")
root.mainloop()