# 简介
一个简单的python脚本，用于实现对GitHub和Gitbook下的双推。

# 下载
点击右下角的`Clone in Desktop`或者`Download Zip`将代码下载到本地。
或者使用命令行命令
```
git clone https://github.com/wp-lai/double_push.git
```

# 使用
将`double_push.py`移动到使用git的文件夹里。然后在命令行里执行
```
python double_push.py
```

接着会出现提示，让你输入：
1. GitHub和Gitbook上的用户名
2. GitHub上代码库的名称，如果是"OMOOC2py"，直接点击回车
3. Gitbook上书籍的名称，如果是"OMOOC2py"，直接点击回车

命令执行成功会显示`Mission Complete`

这之后，本地代码库进行修改并完成commit之后
执行`git push`，就可以同时push给GitHub和Gitbook

此外，也可以直接调用`double_push`库里面的`add_pushurl`函数，例如
```python
import double_push

double_push.add_pushurl(wp-lai, OMOOC2py, OMOOC2py)
```

# 注意事项
1. 确认在GitHub和Gitbook里已经建立了相应的代码库，若没有的话，新建一个即可。

2. 脚本命令执行时，shell的当前工作文件夹需是代码文件夹。Mac下用`pwd`可以显示shell的当前目录，如果不是代码文件夹，则用`cd`命令更改shell的当前文件夹。



# 改进和建议
欢迎大家在issue中指出代码问题和提出修改建议，也希望大家fork以及提交pull request。

# CHANGELOG
**Version 1.0**
*Oct 16, 2015*
> 第一版发布

**Version 1.1**
*Oct 17, 2015*

> + 将主要内容写进一个函数里，这样用户可以把double_push当作一个模块，调用里面add_pushurl()函数
> + 将从命令行命令里获得用户输入改为通过交互问答获得用户输入
