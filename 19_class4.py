#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 20:09
# @Author  : zengxt
# @File    : 16_class.py


class Person:
    # Python对象创建的时候，先执行的是 __new__ 方法，然后调用 __init__ 方法进行对象的初始化
    def __new__(cls, *args, **kwargs):
        print('__new__ 被调用执行，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建对象的id为：{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        # self 对象绑定的就是 __new__ 方法创建的对象
        print('__init__ 被调用执行，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age

    def hello(self):
        print('my name is ', self.name, ", i'am ", self.age, 'years old.')


print('object这个类的id值为：{0}'.format(id(object)))
print('Person这个类的id值为：{0}'.format(id(Person)))

p1 = Person('李四', 34)
print('p1实例的id为{0}'.format(id(p1)))


print("=============================================")
p2 = Person('李四', 34)
print('p2实例的id为{0}'.format(id(p2)))
