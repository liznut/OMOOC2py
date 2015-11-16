#本周整体任务概述:

在上周开发基础上, 完成 极简交互式笔记的网络版本

需求如下:

每次运行时合理的打印出过往的所有笔记

一次接收输入一行笔记

在服务端保存为文件:

在所有访问的客户端可以获得历史笔记


支持多个客户端同时进行笔记记录

UDP 协议

网络数据传输

C/S 架构实现

网络应用调试技巧

(网络抓包分析)

MyDailyNet 私人记事本内网CLI版

##UDP协议

User Data Protocol，用户数据报协议:又称使用者资料包协定，是一个简单的面向数据报的传输层协议。

##python.socket函数：

http://hackerxu.com/2014/11/28/python_socket.html 

##套接字家族：

基于文件型：AF_UNIX或者AF_LOCAL

基于网络型：AF_INET或者AF_INET6或者AF_NETLINK

AF_INET家族可以分为3种,我们常用的就两种TCP和UDP,对应的套接字类型为SOCK_STREAM和SOCK_DGRAM

##python 写server的步骤：

http://openexperience.iteye.com/blog/145701
	
1.创建socket对象。调用socket构造函数。如：socket=socket.socket(family,type) family 代表地址家族，可为AF_INET或AF_INET。AF_INET家族包括Internet地址，AF_UNIX家族用于同一台机器上的进程间通信。type参数代表套接字类型，可为SOCK_STREAM(流套接字)和SOCK_DRAM(数据报套接字)。

2.将socket绑定到指定地址。这是通过socket对象的bind方法来实现的：
socket.bind(address)
由AF_INET所创建的套接字，address地址必须是一个双元素元组，格式是(host，port)。host代表主机，port代表端口号。如果端口号正在使用、主机名不正确或端口已被保留，bind方法将引发socket。error异常。

3.使用socket套接字的listen方法接收连接请求。socket.listen(backlog)  backlog 指定最多允许多少个客户连接到服务器。他的值至少为1。收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求。

4.服务器套接字通过socket.accept方法等待客户请求一个连接。
	
	connection，address=socket.accept()

调用accept方法时，socket会进入waiting状态，客户请求连接时，方法建立连接并返回服务器。accept方法返回一个含有两个元素的元组(connection,address)。第一个元素connection是新的socket对象，服务器必须通过它与客户通信；第二个元素address是客户的Internet地址。

5.第五步是处理阶段，服务器和客户端通过send和recv方法通信(传输数据)。服务器调用send，并采用字符串形式向客户发送信息。send方法返回已发送的字符个数。服务器使用recv方法从客户接受信息。调用recv时，服务器必须指定一个整数，它对应于可通过本次方法调用来接受的最大数据量。recv方法在接收数据时会进入blocked状态，最后返回一个字符串，用它表示收到的数据。如果发送的数据量超过了recv所允许的，数据会被截短。多余的数据将缓冲于接收端。以后调用recv时，多余的数据会从缓冲区删除(以及自上次调用recv以来，客户可能发送的其他任何数据)。

6.传输结束，服务器调用socket的close方法关闭连接。

##python写client的步骤：

1.创建一个socket以连接服务器：socket=socket.socket(family,type)


2.使用socket的connect方法连接服务器。对于AF_INET家族，连接格式如下：
socket.connect(host，port)
host 代表服务器主机名或IP，port代表服务器进程所绑定的端口号。如连接成功，客户就可通过套接字与服务器通信，如果连接失败，会引发socket.error异常。

3.处理阶段，客户和服务器将通过socket方法和recv方法通信。

4.

传输阶段，客户通过调用socket的close方法关闭连接。

##C/S结构

http://baike.baidu.com/view/268856.htm?fromtitle=C%2FS&fromid=826311&type=syn

即大家熟知的客户机和服务器结构。它是软件系统体系结构，通过它可以充分利用两端硬件环境的优势，将任务合理分配到Client端和Server端来实现，降低了系统的通讯开销。目前大多数应用软件系统都是Client/Server形式的两层结构，由于现在的软件应用系统正在向分布式的Web应用发展，Web和Client/Server 应用都可以进行同样的业务处理，应用不同的模块共享逻辑组件；因此，内部的和外部的用户都可以访问新的和现有的应用系统，通过现有应用系统中的逻辑可以扩展出新的应用系统。这也就是目前应用系统的发展方向




