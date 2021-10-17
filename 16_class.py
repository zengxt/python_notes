#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 20:09
# @Author  : zengxt
# @File    : 16_class.py


class Student:
    # 直接写在类里面的变量，成为类属性
    home = '江西'

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def hello(self):
        print('Student Hello World!!')

    # 类方法
    @classmethod
    def clsmethod(cls):
        print("@classmethod修饰的方法为类方法，默认参数为 cls")

    # 静态方法
    @staticmethod
    def staticmethod():
        print('@staticmethod修饰的方法为静态方法，不需要self方法！')


print(Student)
print(id(Student))
print(type(Student))
print(Student.home)
Student.staticmethod()
Student.clsmethod()

print()
print('对象的创建=====')
stu1 = Student('张三', 20)
print(stu1)
print(id(stu1))
print(type(stu1))
print('===========================')
print(stu1.home)
print(stu1.name)
print(stu1.age)
stu1.hello()
Student.hello(stu1)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
stu2 = Student('李四', 30)
stu2.gender = '男'  # 为对象动态绑定属性，该属性只属于 stu2对象
print(stu1.name, stu1.age)
# print(stu1.gender)  # AttributeError: 'Student' object has no attribute 'gender'
print(stu2.name, stu2.age, stu2.gender)


# 为对象动态绑定方法
def show():
    print('定义在类之外的方法！')
stu2.show = show
stu2.show()
