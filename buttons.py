from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import sys

app = Tk()
app.title("panipuri converter")


app.geometry('950x450')
abc=StringVar()

def beenclicked():
	#md=open("abc.md",'w')
	#tex=open("latex.tex",'w')
	#tex = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".tex")


	#lines=md.read()

	#for line in lines:
	#	tex.write(lines)

	text1.delete('1.0', END) 
	abc=text2.get("1.0",END)
	tkinter.messagebox.showinfo(title="compiling", message ="done with sucess")
	text1.insert(INSERT,'\\begin{document}\n\n')
	text1.insert(INSERT,abc)
	text1.insert(INSERT,'\end{document}')
	#md1.write(abc)
	#md.close
	#tex.close()
	return

def quit():
	mexit =tkinter.messagebox.showwarning(title="quit",message="Are you sure you want to quit?")
	app.destroy()
		
def nopen():
	text2.delete('1.0', END) 
	fin=open(tkinter.filedialog.askopenfilename(filetypes= (("md files","*.md"),("All files","*.*"))),'r')
	lines=fin.read()
	for line in lines:
		text2.insert(INSERT,lines)
		return 

 	
def savemd():
      """get a filename and save the text in the editor widget"""
      # default extension is optional, here will add .txt if missing
      md = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".md")
      text2save = str(text2.get(0.0,END))
      md.write(text2save)
      md.close()
 
 
def savetex():
	tex = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".tex")
	abc=text2.get("1.0",END)
	tkinter.messagebox.showinfo(title="saving tex file", message ="saved!!! :D")
	text2save = str(text1.get(0.0,END))
	tex.write(text2save)
	tex.write('\documentclass{article}\n \n \\begin{document}\n')
	tex.write(abc)
	tex.write('\n\n\end{document}\n')
	tex.close()
 	   
def nNew():
	mlabel =Label(app,text="new").pack()
	text1.delete('1.0', END) 
	text2.delete('1.0', END) 
	return

def help():
	tkinter.messagebox.showinfo(title="Help", message ="**Markdown** allows you to write using an easy-to-read, easy-to-write plain text format, then convert it to structurally valid XHTML (or HTML) whereas **LaTeX** is a document preparation system and document markup language.")
	return
	
def run():
     text1.insert(INSERT,text2.get("1.0",END))
     return 




run= Button(app, text = "run",activebackground='blue', width = 5,command = beenclicked).pack(side=TOP, fill='both')
#button3= Button(app, text = "quit",activebackground='blue',width = 5,command = quit).pack(side=TOP)
	
menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=nNew)
filemenu.add_command(label="Open", command=nopen)
filemenu.add_command(label="Save md file", command=savemd)
filemenu.add_command(label="Save tex file. ..", command=savetex)
filemenu.add_command(label="Close", command=quit)

#filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
#editmenu.add_command(label="Undo", command=quit)
#editmenu.add_separator()



#editmenu.add_command(label="Cut", command=quit)
#editmenu.add_command(label="Copy", command=quit)
#editmenu.add_command(label="Paste", command=quit)
#editmenu.add_command(label="Delete", command=quit)
#editmenu.add_command(label="Select All", command=quit)
#menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="documentation", command=help)
helpmenu.add_command(label="About...", command=help)
menubar.add_cascade(label="Help", menu=helpmenu)
app.config(menu= menubar)


	
text2 = Text(app)
text2.pack(side='left',fill='both')


text1 = Text(app)
text1.pack(side='right',fill='both')



#text1.config(width=150,height=30)
scrl = Scrollbar(app, command=text2.yview)
text2.config(yscrollcommand=scrl.set)
scrl.pack(side=LEFT,fill='y',expand='50')
scrl2 = Scrollbar(app, command=text1.yview)
text1.config(yscrollcommand=scrl2.set)
scrl2.pack(side=RIGHT,fill='y',expand='50')



app.mainloop()
