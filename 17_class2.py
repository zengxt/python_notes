#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 20:09
# @Author  : zengxt
# @File    : 16_class.py


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 加两个 _ 修饰，表示类的私有变量，只能在类里面访问

    def hello(self):
        print('my name is ', self.name, ", i'am ", self.__age, 'years old.')


stu1 = Student('张三', 20)
print(stu1.name)
# print(stu1.__age)  # AttributeError: 'Student' object has no attribute '__age'
stu1.hello()

# dir 列出该对象的所有属性
print(dir(stu1))
print(stu1._Student__age)  # 也能访问，但是不建议
