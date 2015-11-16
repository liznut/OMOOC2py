# -*- coding: utf-8 *-*

from bottle import route,debug,run,template,post,request
@route('/diary')
def write_diary():
	return'''
		<form method="POST">
				写下日记:<input name="diary"  type="text"/>
				<input value="submit diary" type="submit"/>
		</form>
	'''
@post('/diary')
def read_diary():
	diary=request.forms.get('diary')
	return '<p>This is your diary:<b>%s</b> </p>' %(diary)
debug(True)
run(host='localhost',port=8080,reloader=True)

