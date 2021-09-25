#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 16:19
# @Author  : zengxt
# @File    : 11_set.py

# Python 中的集合也是可变的，可以理解为没有value的键值对（字典）
set1 = {'python', 'set', 100, 'set'} # 集合中的元素和dict中一样，不能重复，无需
print(set1, type(set1))
set2 = set(['python', 'set', 100]) # set 函数的入参可以是一个list，也可以是一个元组
print(set2, type(set2))
set3 = set(('python', 'set', 100, 100, 34, 100))
print(set3, type(set3))

set4 = set('python')
print(set4, type(set4))

# 空集合， {} 是空字典
set5 = set()
print(set5, type(set5))

print('=========================集合的添加操作==========================')
set5.add(200)  # add 一次添加一个元素
print(set5)

set5.update({300, 400, 500})  # update() 最少添加一个元素
print(set5)
set5.update(range(100, 110))
print(set5)


print('=========================集合的删除操作==========================')
# remove() 方法，一次删除一个指定的元素，如果指定的元素不存在抛出 KeyError
# discard() 方法，一次删除一个指定元素，如果指定的元素不存在不抛出异常
# pop() 方法，一次随机删除一个元素
# clear() 方法，清空集合
set5.remove(100)
print(set5)
set5.discard(101)
set5.discard(101)
print(set5)
set5.pop()
set5.pop()
print(set5)

set5.clear()
print(set5)


print('=========================集合之间的关系==========================')
s1 = {10, 20, 30, 40}
s2 = {40, 30, 10, 20}
print(s1 == s2)  # 是否相等，判断的是集合中的元素

s3 = {10, 20, 90}
print(s3.issubset(s1))  # 一个集合是否是另一个的子集
print(s2.issubset(s1))

print(s1.issuperset(s3))  # 一个集合是否是另一个超集
print(s1.issuperset(s2))

print(s1.isdisjoint(s3))  # 是否没有交集， True：表示两个集合没有交集，False：两个集合有交集


print('=========================集合的数学操作==========================')
s4 = {10, 20, 30, 40}
s5 = {20, 30, 40, 50, 60}

# 交集
print(s4.intersection(s5))
print(s4 & s5)  # 取交集操作 intersection 与 & 相同

# 并集
print(s4.union(s5))
print(s4 | s5)  # 取并集操作 union 与 | 相同

# 差集
print(s4.difference(s5))
print(s4 - s5)  # 取差集操作 difference 与 - 相同

# 对称差集 (两个几个的并集减去两个集合的交集)
print(s4.symmetric_difference(s5))
print(s4 ^ s5)  # 取对称差集的操作 symmetric_difference 与 ^ 相同

# 所有的集合操作都不会改变原集合
print(s4)
print(s5)


print('=========================集合生成式==========================')
# 列表生成式
lst = [i*i for i in range(1, 11)]
print(lst)

# 集合生成式
st = {i*i for i in range(1, 11)}
print(st)