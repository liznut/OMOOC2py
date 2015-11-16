#http://blog.csdn.net/xiaoguaihai/article/details/43339335

from bottle import route,run,template

@route('/helloworld/:yourwords',method=['GET','POST'])
def hello(yourwords):
	return 'hello world.'+ yourwords

run(host='localhost',port=8080)

