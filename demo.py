#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/12 23:17
# @Author  : zengxt
# @File    : demo.py

num = int(input('请输入一个十进制整数：'))
# bin 获取一个数字的二进制表示
print(num, '的二进制表示为：', bin(num))
print(str(num) + ' 的二进制表示为：' + bin(num))
print('%s 的二进制表示为：%s' % (num, bin(num)))
print('{0} 的二进制表示为：{1}'.format(num, bin(num)))
print(f'{num} 的二进制表示为：{bin(num)}')

# oct 获取一个数字的八进制
print(f'{num} 的二进制表示为：{oct(num)}')
# hex 获取一个数字的十六进制
print(f'{num} 的二进制表示为：{hex(num)}')


# isdigit 判断是否是一个数字
print('888w'.isdigit())

import random

# random 用于生成随机数
print(random.random())
print(random.randint(1000, 1500))

# chr() 获取 ASCII 码值对应的字符
index = 1
while index < 128:
    print(chr(index), '-->', index)
    index += 1
