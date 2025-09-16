# 第四章 相关代码编译
本章节主要描述开发板相关源码的编译方法，包括内核源码编译、应用程序编译方法。注意：当前只提供了内核源码，本节只介绍内核和应用程序的编译方法

## 4.1编译前准备
### 4.1.1 环境说明
+ 开发环境操作系统：Ubuntu22.04  64位版
+ 交叉工具链：aarch64-none-linux-gnu
+ 开发板使用Bootloader 版本：u-boot-2017.09
+ 开发板内核版本：linux-6.1.57

### 4.1.2 拷贝源码
+ 程序源码：用户资料\Linux\源码\

创建工作目录

forlinx@ubuntu:~$ <font style="color:#0000FF;">mkdir -p /home/forlinx/3576						</font>//按照顺序创建工作目录

将用户资料中的源码文件和交叉编译工具链拷贝到虚拟机/home/forlinx/3576目录。

forlinx@ubuntu:~$ <font style="color:#0000FF;">cd /home/forlinx/3576									</font>//切换到工作目录

forlinx@ubuntu:~/3576$ <font style="color:#0000FF;">cat OK3576_linux_source.tar.bz2.0* >OK3576_linux_source.tar.bz2   </font>//在当前位置解压压缩包

forlinx@ubuntu:~/3576$<font style="color:#0000FF;"> tar -vxf</font> <font style="color:#0000FF;">OK3576_linux_source.tar.bz2</font>

运行命令后等待完成即可。

## 4.2 源码编译
+ **注意：**

<font style="color:#000000;"> </font>**整体编译过后，可根据实际情况再进行单独编译 **

<font style="color:#000000;"> </font>**该源码编译需要开发环境运行内存 8G 及以上，请不要修改我们提供的 VM 虚拟机镜像配置**

**4.2.1 全编译测试**

<font style="color:#000000;">在源码路径内，提供了编译脚本 build.sh，运行该脚本对整个源码进行编译，需要在终端切换到解压 </font>

<font style="color:#000000;">出来的源码路径，找到 build.sh 文件。 </font>

| **forlinx@ubuntu: ~/3576$ ****<font style="color:#0000FF;">cd OK3576_linux_source/                     </font>****// 跳转到源码路径** |
| --- |


<font style="color:#000000;">以下操作需要在源码目录下操作，全编译方法：</font>

| **forlinx@ubuntu: ~/3576$ ****<font style="color:#0000FF;">./build.sh chip </font>****                       //设置环境变量 ，这里选择ok3576**<br/>**forlinx@ubuntu: ~/3576$****<font style="color:#0000FF;"> ./build.sh                                </font>****//进行全编译**<br/> |
| --- |


**编译完成后，系统镜像会在output/update/image/ 文件夹中生成update.img**

**<font style="color:#000000;">注</font>****意：update.img 为打包好用于 OTG 或者 TF 卡完全烧写用，其它文件为分步烧写使用**

**4.2.2 单独编译**





| **forlinx@ubuntu: ~/3576$ ****<font style="color:#0000FF;">cd OK3576_linux_source/                     </font>****// 跳转到源码路径**<br/>**forlinx@ubuntu: ~/3576$ ****<font style="color:#0000FF;">./build.sh chip </font>****                       //设置环境变量 ，这里选择ok3576**<br/>**forlinx@ubuntu: ~/3576$****<font style="color:#0000FF;"> ./build.sh kernel                                 </font>****//编译内核**<br/>**//编译完成后，在kernel/路径生成boot.img。** |
| --- |
|  |


<font style="color:#000000;">编译成功后 update.img 里的内核不更新。请分步烧写 kernel/boot.img 文件。</font>参考用户使用手册OTG烧写测试章节，使用生成的boot.img替换默认出厂镜像烧写即可。

**4.2.3 清除编译生成的文件**

<font style="color:#000000;">用户在源码路径下进行操作</font>

| **forlinx@ubuntu: ~/3576$ .****<font style="color:#0000FF;">/build.sh cleanall               </font>****// 清理编译生成的所有文件** |
| --- |
|  |


## 4.3 应用程序编译及运行
### 4.3.1 编译并运行命令行应用
本小节使用飞凌看门狗测试程序做演示，也可以自行构建工程。 

1、使用cd命令进入/home/forlinx/3576目录

| forlinx@ubuntu:~$ <font style="color:#0000FF;">cd OK3576_linux_source/app/forlinx/forlinx_cmd/fltest_watchdog</font> |
| --- |


2、配置交叉编译器路径，使用make进行交叉编译

| forlinx@ubuntu:~/3576/OK3576_linux_source/app/forlinx/forlinx_cmd/fltest_watchdog$ <font style="color:#0000FF;">export CROSS_COMPILE=/home/forlinx/3576/aarch64-buildroot-linux-gnu_sdk-buildroot</font><br/><font style="color:#0000FF;">/bin/aarch64-buildroot-linux-gnu-</font><br/>forlinx@ubuntu:~/3576/OK3576_linux_source/app/forlinx/forlinx_cmd/fltest_watchdog$ <font style="color:#0000FF;">export PATH=$PATH:/home/forlinx/3576//aarch64-buildroot-linux-gnu_sdk-buildroot</font><br/><font style="color:#0000FF;">/bin/</font><br/>修改Makefile的cpp选项为<font style="color:#0000FF;"> CPP=$(CROSS_COMPILE)gcc</font><br/>forlinx@ubuntu:~/3576/OK3576_linux_source/app/forlinx/forlinx_cmd/fltest_watchdog$ <font style="color:#0000FF;">make	</font><br/>aarch64-none-linux-gnu-gcc watchdog.c -o fltest_watchdog<br/>generate fltest_watchdog success!!! |
| --- |


用file命令查看生成的文件信息

| forlinx@ubuntu:~/3576/OK3576-linux-source/app/forlinx/forlinx_cmd/fltest_watchdog$ <br/><font style="color:#0000FF;">file fltest_watchdog </font><br/>fltest_watchdog: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, for GNU/Linux 3.7.0, with debug_info, not stripped |
| --- |


通过结果可以看到编译生成的是64位、ARM的文件。

3、将编译生成的fltest_watchdog通过U盘或者ftp等方式拷贝到板子上，比如/forlinx路径下，下述以tf卡为例，拷贝到开发板，运行测试。

| [root@ok3576:/]# <font style="color:#0000FF;">cp /run/media/mmcblk1p1/fltest_watchdog /home/forlinx</font><br/>[root@ok3576:/]# <font style="color:#0000FF;">cd /home/forlinx</font><br/>[root@ok3576:/home/forlinx]#<font style="color:#0000FF;"> ./fltest_watchdog</font><br/>Watchdog Ticking Away! |
| --- |


1. 参考用户使用手册“看门狗测试”章节测试。

## 4.4 Qt Creator 环境配置 
### 4.4.1 交叉编译器配置 
注意：默认的开发环境已经安装了交叉编译链，如果自己搭建的开发环境，需要参考 3.3 安装交叉编 

译链安装交叉编译链（默认安装路径为/home/forlinx/aarch64-buildroot-linux-gnu_sdk-buildroot）

Qt的版本是Qt 5.15.11

<font style="color:#000000;">Qt 是跨平台的图形开发库，支持众多操作系统，在进行编译前需要对 Qt Creator 的编译环境进行配置。</font>

<font style="color:#000000;">1、进入 qtcreator 的安装路径打开 qtcreator</font>

| forlinx@ubuntu:<font style="color:#000000;">~/qtcreator-4.7.0/bin$ </font><font style="color:#0000FF;">./qtcreator &</font> |
| --- |


<font style="color:#000000;">2、点击 Qt Creator 的 Tools ->Options->Kits->Compilers， 然后点击 Add ->GCC->C； </font>

<font style="color:#000000;">3、Name 输入 GCC； </font>

<font style="color:#000000;">4、将编译链的路径粘贴到 Compiler Path 如下图所示：</font>

<font style="color:#000000;"> </font><font style="color:#0000FF;">路径：/home/forlinx/aarch64-buildroot-linux-gnu_sdk-buildroot/bin/aarch64-linux-gcc</font>

![](https://cdn.nlark.com/yuque/0/2024/png/45535139/1726292014485-f06907c5-932b-4414-80ff-d76ced326a9a.png)

<font style="color:#000000;">5、按照同样的方法添加 GCC 编译器，点击右侧“Add->GCC->C++”，如图所示： </font>

<font style="color:#000000;"> </font><font style="color:#0000FF;">路径：/home/forlinx/aarch64-buildroot-linux-gnu_sdk-buildroot/bin/aarch64-linux-g++</font>

![](https://cdn.nlark.com/yuque/0/2024/png/45535139/1726292014769-384507d5-8651-47a2-93a8-c288b8a17df3.png)



### 4.4.2 Qt Versions 配置 
<font style="color:#000000;">1、点击 Qt Creator 的 Tools ->Options->Qt Versions， </font>

<font style="color:#000000;">2、然后点击 Add，弹出对话框选择</font><font style="color:#0000FF;">/home/forlinx/aarch64-buildroot-linux-gnu_sdk-buildroot/bin/qmake </font>

<font style="color:#000000;">3、点击 open 添加。 </font>

<font style="color:#000000;">4、然后会返回 Qt Version 配置框，Version name 可以自行更改。 </font>

<font style="color:#000000;">5、然后点击 Apply 及 OK。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/45535139/1726292015054-64cf2592-9fbc-4fa7-9c02-5167becea1fe.png)

### 4.4.3 Kits 配置 
<font style="color:#000000;">Kits 是一个构建套件，用来构建和选择开发编译环境，对于有多种 QT 库的项目很有用。将之前添加 </font>

<font style="color:#000000;">的交叉编译器和 QT Version 添加到 Kits 中，构建适合开发板的编译环境。 </font>

<font style="color:#000000;">1、点击 Qt Creator 的 Tools ->Options->Kits， 然后点击 Add，出现配置部分。 </font>

<font style="color:#000000;">2、Name 自行更改。 </font>

<font style="color:#000000;">3、Compiler 选择 GCC。 </font>

<font style="color:#000000;">4、Qt ve</font>rsion 选择 Qt version 创建时输入的名字。 

5、然后点击 Apply 及 OK。

![](https://cdn.nlark.com/yuque/0/2024/png/45535139/1726292015332-5cb82538-73e7-437c-9e21-ede225f2efcb.png)





