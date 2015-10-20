# all about sublimetext
##一个想法：既然sublimetext 是一个文本编辑器，那么我除了用它来编写程序以外应该可以用来编辑文字，像使用txt一样，这样可以更加方便记录学习过程中的各种想法。

### 成功了，好开心~~

##一个问题：
###由于没有交互功能，在使用带有raw_input的命令时，python 会报错：EOFError: EOF when reading a line
###为了实现python 交互命令，使用REPL插件，但是总是报错：
sublime WindowsError(2,'\xcf\xb5\xcd\xb3\xd5\xd2\xb2\xbb\xb5\xbd\xd6\xb8\xb

###Google 之，找到教程：
1.http://blog.csdn.net/angelahhj/article/details/42172487
2.http://stackoverflow.com/questions/19734343/sublime-text-2-sublimerepl-package-issue
（这个方法可以给REPL设置快捷键）
3.http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7

###检查：
####	在sublimetext中输入 pyhon后，得到
			[Error 2] 
		[cmd:  [u'python', u'-u', u'']]
		[dir:  E:\course documents\py]
		[path: D:/python2.7.10]
		[Finished]
    环境变量已设置

### 我尝试了很多方法都失败了，最后找到了这条：https://github.com/wuub/SublimeREPL/issues/96
###成功

##于是sublimetext 能够实现python交互功能。此时，运行代码使用"ctrl+shift+R" 而不是"ctrl +B"

###还有一些关于REPL的设置可以参考：http://koko.ntex.tw/wordpress/sovle-sublime-python-eof-when-reading-a-line-using-sublimerepl/

