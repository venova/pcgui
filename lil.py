import Tkinter
import tkMessageBox
import sys
from Tkinter import *
import tkFileDialog
from tkFileDialog import askopenfilename
#import sys

app = Tkinter.Tk()
app.title("panipuri converter")


app.geometry('950x450')
abc=Tkinter.StringVar()

def beenclicked():
	text1.delete('1.0', END) 
	abc=text2.get("1.0",END)
	tkMessageBox.showinfo(title="compiling", message ="done with sucess")
	text1.insert(INSERT,'\\begin{document}\n\n')
	text1.insert(INSERT,abc)
	text1.insert(INSERT,'\end{document}')
	
	#md1.write(abc)
	#md.close
	#tex.close()
	return

def quit():
	mexit =tkMessageBox.ask(title="quit",message="Are you sure you want to quit?")
	return
		
def nopen():
	text2.delete('1.0', END) 
	fin=open(tkFileDialog.askopenfilename(filetypes= (("md files","*.md"),("All files","*.*"))),'r')
	lines=fin.read()
	for line in lines:
		text2.insert(INSERT,lines)
		return 

 	
def savemd():
      """get a filename and save the text in the editor widget"""
      # default extension is optional, here will add .txt if missing
      md = tkFileDialog.asksaveasfile(mode='w', defaultextension=".md")
      text2save = str(text2.get(0.0,END))
      md.write(text2save)
      md.close()
 

def savetex():
	tex = tkFileDialog.asksaveasfile(mode='w', defaultextension=".tex")
	abc=text2.get("1.0",END)
	tkMessageBox.showinfo(title="saving tex file", message ="saved!!! :D")
	text2save = str(text1.get(0.0,END))
	tex.write(text2save)
	tex.write('\documentclass{article}\n \n \\begin{document}\n')
	tex.write(abc)
	tex.write('\n\n\end{document}\n')
	tex.close()
	   
def nNew():
	mlabel =Tkinter.Label(app,text="new").pack()
	#text2.del()
	text2.delete('1.0', END) 
	text1.delete('1.0', END) 
	#text2.insert(INSERT," ")
	return

def help():
	app1 =Tkinter.Tk()
	app1.title("readme")
	app1.geometry('350x550')
	#labelText = StringVar()
	#labelText.set('click :D :D :D')
	#label1 = Label(app1, textvariable = labelText, height = 4)
	#label1.pack(side="top",fill="both")
	text3 = Tkinter.Text(app1)
	text3.pack(fill="both",expand=50)
	text3.insert(INSERT,'**Markdown** allows you to write using an easy-to-read,\n easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML) \nwhereas **LaTeX** is a document preparation system and document markup language."')
	return

run= Tkinter.Button(app, text = "run",activebackground='blue', width = 5,command = beenclicked).pack(side="top", fill='both')

#button3= Button(app, text = "quit",activebackground='blue',width = 5,command = quit).pack(side=TOP)
	
menubar = Tkinter.Menu(app)
filemenu =Tkinter. Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=nNew)
filemenu.add_command(label="Open", command=nopen)
filemenu.add_command(label="Save md file", command=savemd)
filemenu.add_command(label="Save tex file. ..", command=savetex)
filemenu.add_command(label="Close", command=quit)

#filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)
editmenu =Tkinter. Menu(menubar, tearoff=0)
#editmenu.add_command(label="Undo", command=quit)
#editmenu.add_separator()



#editmenu.add_command(label="Cut", command=quit)
#editmenu.add_command(label="Copy", command=quit)
#editmenu.add_command(label="Paste", command=quit)
#editmenu.add_command(label="Delete", command=quit)
#editmenu.add_command(label="Select All", command=quit)
#menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="documentation", command=help)
helpmenu.add_command(label="About...", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)
app.config(menu= menubar)



text2 = Tkinter.Text(app)
text2.pack(side='left',fill='both',padx=5,pady=5)


text1 = Tkinter.Text(app)
text1.pack(side='right',fill='both',padx=5,pady=5)



#text1.config(width=150,height=30)
scrl = Tkinter.Scrollbar(app, command=text2.yview)
text2.config(yscrollcommand=scrl.set)
scrl.pack(side="left",fill='y', expand='10')
scrl2 =Tkinter. Scrollbar(app, command=text1.yview)
text1.config(yscrollcommand=scrl2.set)
scrl2.pack(side="right",fill='y',expand='50')


app.mainloop()
