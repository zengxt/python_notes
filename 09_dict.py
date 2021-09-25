#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 14:46
# @Author  : zengxt
# @File    : 09_dict.py

# Python 中的字典和列表一样都是可变序列，字典以键值对的方式存储数据
print('===========================字典的创建=============================')
person = {'name': '张三', 'age': 23}
print(person)
print(type(person))

scores = dict(张三=23, 李四=67, Tome=90)
print(scores)


print('===========================字典元素的获取=============================')
print(scores['张三'])
print(scores.get('张三'))
# print(scores['马琪']) # KeyError: '马琪'， 使用[] 获取字典中的值，如果key不存在，会报错
print(scores.get('马琪'))  # 使用get获取字典中的值，如果key不存在，返回None
print(scores.get('马琪', 100))  # 如果key不存在，返回指定的默认值


print('===========================字典元素的增删改=============================')
print('张三' in scores)  # 判断键值在字典中是否存在
print('张三' not in scores)

del scores['张三']  # 删除字典中的元素
print('张三' in scores)

scores['程六'] = 98  # 增加元素
print(scores)

scores['程六'] = 100  # 修改元素
print(scores)
# scores.clear() 清空字典

print('===========================字典的视图=============================')
keys = scores.keys()
print(keys, type(keys), list(keys))
values = scores.values()
print(values, type(values), list(values))
items = scores.items()  # 获取字典的key-value对
print(items, type(items), list(items))


print('===========================字典的遍历=============================')
for item in scores:  # 遍历的item是字典中的key
    print(item, scores[item], scores.get(item))


print('===========================字典生成式=============================')
# 内置函数zip()：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
things = ['Fruits', 'Books', 'Others']
prices = [97, 68, 90]
test = {thing: price for thing, price in zip(things, prices)}  # zip 函数会以短的列表为准
print(test)
