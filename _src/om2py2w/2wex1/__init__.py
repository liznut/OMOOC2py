# -*- coding:utf-8 -*-

##在上周开发基础上, 完成 极简交互式笔记的桌面版本

#需求如下:

#1 每次运行时合理的打印出过往的所有笔记

#2 一次接收输入一行笔记

#3 保存为本地文件
from Tkinter import*
import time
import os
import sys;
reload(sys);
root=Tk()

def key(event):
	print"pressed",repr(event.char)

def saveClick(event):
	with open(os.getcwd()+r'diary','w+') as fb:
		fb.write(text.get(0.0,'end'))

frame=Frame(root,width=300,height=300)
frame.pack()

text=Text()

text.insert(INSERT,"this is text......")

text.bind("<Return>",key)
text.pack()

button=Button(frame,text='save')

button.bind("<Button-1>",saveClick)
button.pack()

root.mainloop()
