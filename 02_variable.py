#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/21 0:58
# @Author  : zengxt
# @File    : 02_variable.py

# 1、变量的属性
name = 'string'
# 一个变量有 地址（标识）、类型、值 三个属性
print('标识', id(name))
print('类型', type(name))
print('值', name)

# 2、字符型，可以使用单引号、双引号、三引号（三个单引 或者 三个双引）
print('三引号可以换行输出', '''hello 
                   , word''')

# 3、python中的整数可以表示为二进制（0b）、十进制、八进制（0o）、十六进制（0x）
print('十进制', 123)
print('二进制', 0b10101111)
print('八进制', 0o176)
print('十六进制', 0x1EAF)

# 4、浮点类型，浮点的存储不精确
f1 = 1.1
f2 = 2.2
f3 = 2.1
print(f1 + f2)
print(f1 + f3)

# 使用 Decimal 模块可以得到精确的结果
from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))

# 5、布尔类型
bool1 = True
bool2 = False
print(bool1, type(bool1))
print(bool2, type(bool2))
print(bool1 + 1)  # bool 和数字可以相互转换，True表示1，False表示0
print(bool2 + 1)

# 数据类型转换
name = '张三'
age = 23
print(type(name), type(age))
# print('姓名: ' + name + ', 年龄: ' + age)  # TypeError: can only concatenate str (not "int") to str
print('姓名: ' + name + ', 年龄: ' + str(age))

# 类型转换
# str() 转换成字符串
# int() 转换成整数，
# 1、字符串必须是整数串，print(int('98.99')) 会报错
# 2、浮点型转成int，会舍弃小数点
print(int('200'))
print(int(99.99))
# float() 转换成浮点型，整数会加 .0
print(float('98.99'))
print(float(2322))
