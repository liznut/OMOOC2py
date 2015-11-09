*本周整体任务概述:

在上周开发基础上, 完成 极简交互式笔记的桌面版本

需求如下:

1 每次运行时合理的打印出过往的所有笔记

2 一次接收输入一行笔记

3 保存为本地文件

*图形用户界面（Graphical User Interface，简称GUI）

是指采用图形方式显示的计算机操作用户界面。与早期计算机使用的命令行界面相比，图形界面对于用户来说在视觉上更易于接受。然而这界面若要通过在显示屏的特定位置，以“各种美观、而不单调的视觉消息”提示用户“状态的改变”，势必得比简单的文字消息呈现，花上更多的电脑运算能力，计算“要改变显示屏哪些光点，变成哪些颜色”。

*GUI programming in python:

Python has a huge number of GUI frameworks (or toolkits) available for it, from TkInter (traditionally bundled with Python, using Tk) to a number of other cross-platform solutions, as well as bindings to platform-specific (also known as "native") technologies.The major cross-platform technologies upon which Python frameworks are based include Gtk, Qt, Tk and wxWidgets, although many other technologies provide actively maintained Python bindings.

*Tkinter:

Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It is a thin object-oriented layer on top of Tcl/Tk.Tkinter is not the only GuiProgramming toolkit for Python. It is however the most commonly used one.

Checking your Tkinter support

1 import _tkinter

2 import TKinter #or import tkinter for V3.0 and later#

3 Tkinter ._test() #or tkinter._test() for V3.0 and later#

*Tcl/Tk:Tcl 是“工具控制语言（Tool Control Language）”的缩写。Tk 是 Tcl“图形工具箱”的扩展，它提供各种标准的 GUI 接口项，以利于迅速进行高级应用程序开发。

Tcl（最早称为“工具命令语言”"Tool Command Language"，但是目前已经不是这个含义，不过我们仍然称呼它为TCL）是一种脚本语言。由John Ousterhout创建。TCL很好学，功能很强大。TCL经常被用于快速原型开发，脚本编程，GUI和测试等方面。TCL念作“踢叩”（tickle）。Tcl的特性包括：

	任何东西都是一条命令，包括语法结构（for,if等）。

	任何事物都可以重新定义和重载。

	所有的数据类型都可以看作字符串。

	语法规则相当简单。

	提供事件驱动给Socket和文件。基于时间或者用户定义的事件也可以。

	动态的域定义。

	很容易用C, C++，或者Java扩展。

	解释语言，代码能够动态的改变。

	完全的Unicode支持。

	平台无关。Win32，UNIX，Mac上都可以跑。

	和GUI紧密集成。Tk 代码紧凑，易于维护。

TCL本身在8.6以后提供面向对象的支持。因为语言本身很容易扩展到支持面向对象，所以在8.6之前存在许多C语言扩展提供面向对象能力，包括XOTcl, Incr Tcl等。另外SNIT扩展本身就是用TCL写的。
使用最广泛的TCL扩展是TK。 

TK提供了各种OS平台下的图形用户界面GUI。Perl、Python等语言都提供接口适配到TK上。另一个流行的扩展包是Expect. Expect提供了通过终端自动执行命令的能力，例如（passwd, ftp, telnet等命令驱动的外壳）.



