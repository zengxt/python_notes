#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 20:05
# @Author  : zengxt
# @File    : os_demo.py.py

# os 模块是 Python 内置的与操作系统功能和文件系统相关的模块，该模块中的语句执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样

# os 模块与 os.path 模块用于对目录或文件进行操作

import os

# 调用系统程序
# os.system('notepad.exe')

# 直接调用系统可执行文件
# os.startfile('D:\\Program Files\\Wechat\\WeChat.exe')

# os 模块常用函数
# getcwd()：返回当前的工作目录
# listdir(path)：返回指定路径下的文件和目录信息
# mkdir(path [,mode])：创建目录
# makedirs(path1/path2...[,mode])：创建多级目录
# rmdir(path)：创建目录
# removedirs(path1/path2......)：删除多级目录
# chdir(path)：将path设置为当前工作目录
print(os.getcwd())

fileList = os.listdir('D://')
print(fileList)

# 删除不存在 或者创建已经存在都会报错
os.rmdir('newdir')
os.mkdir('newdir')
os.removedirs('A/B/C')
os.makedirs('A/B/C')
