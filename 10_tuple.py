#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 15:58
# @Author  : zengxt
# @File    : 10_tuple.py

# 元组 tuple, Python中的不可变序列
tuple1 = ('python', 'tuple', 12, 34)
print(tuple1, type(tuple1))

# 如果元组中只有一个元素，需要在元素后面加上 ',' 否则程序会将其识别为基本数据类型
test = ('python')
print(test, type(test)) # <class 'str'>
tuple2 = ('python',)
print(tuple2, type(tuple2)) # <class 'tuple'>

tuple3 = tuple(('python', 'tuple', 12, 34))
print(tuple3, type(tuple3))

# 空元组
tuple4 = ()
tuple5 = tuple()
print(tuple4, type(tuple4))
print(tuple5, type(tuple5))

print()
print('元组中的元素本身不可变，不能再指向其他元素，但是元组中的元素如果是可变的，则其引用不可变，但是数据可变')
tuple6 = (10, [20, 30], 9)
print(tuple6, type(tuple6))
print(tuple6[0], type(tuple6[0]), id(tuple6[0]))
print(tuple6[1], type(tuple6[1]), id(tuple6[1]))
print(tuple6[2], type(tuple6[2]), id(tuple6[2]))
# 元组中的元素本身不可变
# tuple6[1] = 100 # TypeError: 'tuple' object does not support item assignment
# 元组中的元素如果是可变的，则其引用不可变，但是数据可变
tuple6[1].append(100)
print(tuple6[1], type(tuple6[1]), id(tuple6[1]))

print()
print('元组的遍历')
for item in tuple6:
    print(item)
