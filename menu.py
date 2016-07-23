import Tkinter
from Tkinter import *

def makeMenuBar():    
    # Setup menu bar
	def Open():
	    print "Still in dev"
	def Save():
	    print "Still in dev"
	def About():
	    print "Still in dev"
	
	menubar = Menu(app)
	
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Open", command=Open)
	filemenu.add_command(label="Save", command=Save)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=app.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	
	editmenu = Menu(menubar, tearoff=0)
	editmenu.add_command(label="Cut", command=lambda: app.focus_get().event_generate('<<Cut>>'))
	editmenu.add_command(label="Copy", command=lambda: app.focus_get().event_generate('<<Copy>>'))
	editmenu.add_command(label="Paste", command=lambda: app.focus_get().event_generate('<<Paste>>'))
	menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)
