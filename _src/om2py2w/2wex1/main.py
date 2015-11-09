#！coding:utf8


#import the packages
from Tkinter import *
import time
import os
import sys;


#reload sys
reload(sys);


#default encoding utf8
sys.setdefaultencoding('utf8')


root = Tk()


#keyboard event.


def key(event):
print "pressed", repr(event.char)


#define the button event, save the inputted as file


def saveClick(event):
with open (os.getcwd()+ r'hostb','w+') as fb:
fb.write(text.get(0.0,'end'))


frame = Frame(root, width=300, height=300)
frame.pack()


#frame define text control
text=Text(frame)


#save into 
text.insert(INSERT,"this is text……")


# bind the control event 
text.bind("",key)
text.pack()


#define button 
button=Button(frame,text='save')


#bind events with btn
button.bind("",saveClick)
button.pack()


root.mainloop()
