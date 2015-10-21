# -*- coding:utf-8 -*-

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


 