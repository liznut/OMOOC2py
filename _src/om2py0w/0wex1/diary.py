# -*- coding:utf-8 -*-
#http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820066616a77f826d876b46b9ac34cb5f34374f7a000

def init():
	import sys

	diary = 'this is week1 task of diary\n '

	f = file('diary.txt','w') # open for 'w'riting
	f.write(diary) # write text to file
	f.close() # close the file

def write():
	diaryfile = 'diary.txt'

	while True:
		d = raw_input('diary:')
		if d == '':
			break
		else :
			f = open(diaryfile,'a')
			f.write(d)
			f.write('\n')
	f.close()

def read():
	f = file('diary.txt')

	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print line,
	f.close()


 