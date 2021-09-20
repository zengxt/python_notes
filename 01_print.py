#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/21 0:29
# @Author  : zengxt
# @File    : 01_print.py.py

# 1、简单输出
print(520)
print('hello world')
print("hello \worl'd")
print(12 + 34)

# 2、不换行输出
print('hello', 'world', 'python')

# 3、原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或者R
print(r'hello\nworld')

# 4、输出到文件, print可以有多个参数，指定文件需要指定文件 file=
fp = open('test.txt', 'a+')
print('print to file', file=fp)
fp.close()
