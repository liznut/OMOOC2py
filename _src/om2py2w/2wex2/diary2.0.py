# -*- encoding:utf-8 -*-

from Tkinter import *
root = Tk()

def save():
    text = e.get() + "\n"
    f=open("diary.txt", "a")
    f.write(text)
    f.close()

def read():
	f=open("diary.txt")
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
	f.close

l=Label(root,text='diary')
l.pack()

e=Entry(root)
e.pack()

saveb=Button(root,text='save',command=save)
saveb.pack()

readb=Button(root,text='read',command=read)
readb.pack()

root.mainloop()