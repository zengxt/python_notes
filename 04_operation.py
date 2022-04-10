#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 20:35
# @Author  : zengxt
# @File    : 04_operation.py

# 算术运算符
print(1 / 2)  # 0.5 除法运算
print(11 // 2)  # 5 整除运算
print(11 % 2)  # 1 求余运算
print(2 ** 3)  # 幂运算

print(9 // -4)  # -3 一正一负向下取整

# 赋值运算符，Python中的赋值运算符支持 系列解包赋值 和 链式赋值
a, b, c = 10, 20, 30
print(a, b, c)
e = f = g = 50
print(e, f, g)
# 交换两个变量的值
var1 = '字符'
var2 = 20
print(var1, var2)
var1, var2 = var2, var1
print(var1, var2)

# 比较运算符
# 一个变量有 类型、值、ID 三个属性， == 比较的是值
int1 = 10
int2 = 10
print('int1 == int2 ', int1 == int2)
print('int1 is int2 ', int1 is int2)  # 比较的是ID
list1 = [10, 20, 30, 40]
list2 = [10, 20, 30, 40]
print('list1 == list2 ', list1 == list2)
print('list1 is list2 ', list1 is list2)
print('list1 id is ', id(list1))
print('list2 id is ', id(list2))

# in 操作符
print('ello' in 'helloword')
print('abs' not in 'helloword')

# 位运算
print(4 & 8)  # 0
print(4 | 8)  # 12
print(4 << 1)  # 8 左移位，高位溢出，相当于乘以2
print(4 << 3)  # 32
print(8 >> 1)  # 4 右移位，相当于除以2
