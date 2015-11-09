# -*- coding:utf-8 -*-
#导入需要的包
from Tkinter import *
import time
import os
import sys;

#reload sys
reload(sys);

root = Tk()

#定义键盘时间，敲击键盘，会被打印

def key(event):
	print "pressed", repr(event.char)

#定义save按钮的点击事件，保存内容到文件当中

def saveClick(event):
	with open (os.getcwd()+ r'diary','w+') as fb:
		fb.write(text.get(0.0,'end'))

frame = Frame(root, width=300, height=300)
frame.pack()

#在frame中定义text空间
text=Text(frame)

#放入默认的文案
text.insert(INSERT,"this is text……")

#为text bind事件
text.bind("<Key>",key)
text.pack()

#定义button按钮
button=Button(frame,text='save')

#为按钮绑定事件
button.bind("<Button-1>",saveClick)
button.pack()

root.mainloop()