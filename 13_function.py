#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 23:44
# @Author  : zengxt
# @File    : 13_function.py


# 不可变对象，在函数中改变，实参不会变化，可变对象在函数中改变，实参会随着改变
def fun(args1, args2):
    args1 = 100
    args2.append(args1)


num = 10
lst = [20, 30, 40]
print('函数调用前，num = ', num)
print('函数调用前，lst = ', lst)

fun(num, lst)

print('函数调用后，num = ', num)
print('函数调用后，lst = ', lst)


# 返回多个值，是一个元组
def oddandeven(nums):
    odd = []
    even = []
    for item in nums:
        if item % 2:
            odd.append(item)
        else:
            even.append(item)
    return odd, even


odd, even = oddandeven(range(10))
print(odd, even)


# 形参默认值
def defaultvalue(num1, num2=100):
    print(num1, num2)


defaultvalue(200)
defaultvalue(200, 300)


# * 表示个数可变的位置参数, 结果是一个元组
def params(*args):
    print('个数可变的位置参数', args)


params(10)
params(10, 20)
params(10, 20, 30)


# ** 表示个数可变的关键字形参，结果是一个字典
def params(**args):
    print('个数可变的关键字形参', args)


params(args1=10)
params(args1=10, args2=20)
params(args1=10, args2=20, args3=20)


# 在一个函数中，个数可变的位置形参只能出现一个，个数可变的关键字形参也只能出现一个，
# 如果同时出现在一个函数中，要求个数可变的位置形参 在 个数可变的关键字形参前面
def params(*args1, **args2):
    pass