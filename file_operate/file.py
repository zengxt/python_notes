#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 23:31
# @Author  : zengxt
# @File    : file.py

# 以只读模式打开文件
file = open('data.dat', 'r', encoding='UTF-8')
# 以一个列表的形式返回文件的所有行
print(file.readlines())
file.close()

file1 = open('a.dat', 'w')
file1.write('hello python')
file1.close()

# 使用 with语句（上下文管理器）
# with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确关闭，以此达到释放资源的目的
with open('data.dat', 'r', encoding='UTF-8') as src_file:
    print(src_file.read())


# 上下文表达式，结果为上下文管理器，其本质是一个遵守了上下文管理协议的对象（实现了__enter__() 方法和 __exit()__方法）
class myContext(object):
    def __enter__(self):
        print('进入到 __enter__ 方法！！')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('进入到 __exit__ 方法！！')

    def show(self):
        print('上下文管理器方法')


with myContext() as context:  # 创建上下文时，自动调用 __enter__ 方法，并赋值给 context
    context.show()  # 离开运行上下文时，自动调用 __exit__ 方法
