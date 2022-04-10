#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/10 20:35
# @Author  : zengxt
# @File    : os_path_demo.py

import os.path

# os.path 模块常用方法
# os.path.abspath(path)：用于获取文件或目录的绝对路径
# os.path.exists(path)：用于判断文件或目录是否存在，如果存在返回True，否则返回False
# os.path.join(path, name)：将目录与目录或者文件名拼接起来
# os.path.split()：分离目录和文件名
# os.path.splitext()：分离文件名和扩展名
# os.path.basename(path)：从一个目录中提取文件名
# os.path.dirname(path)：从一个目录中提取文件路径，不包括文件名
# os.path.isdir(path)：用于判断是否是路径

print(os.path.abspath('newdir'))

print(os.path.exists('newdir'))
print(os.path.exists('newdir2'))

print(os.path.join(os.getcwd(), 'test.txt'))

print(os.path.split('D:\Java Program\python_notes\os_module\\test.txt'))
print(os.path.splitext('D:\Java Program\python_notes\os_module\\test.txt'))


# 获取当前路径下所有为 py 文件
fileName = os.listdir(os.getcwd())
for file in fileName:
    if file.endswith(".py"):
        print(file)


print('walk 遍历 ===================================')
# walk 遍历某个目录（包括目录和文件）
fileAndDir = os.walk('D:\Java Program\python_notes')
for dirpath, dirs, files in fileAndDir:
    # 每个目录的路径，该目录下的所有目录和文件
    print(dirpath)
    print(dirs)
    print(files)

    print('%s 目录下的所有的目录：' % (dirpath))
    for dir in dirs:
        print(os.path.join(dirpath, dir))
    print('%s 目录下的所有的文件：' % (dirpath))
    for file in files:
        print(os.path.join(dirpath, file))
    print()
