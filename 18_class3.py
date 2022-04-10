#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 20:09
# @Author  : zengxt
# @File    : 16_class.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print('my name is ', self.name, ", i'am ", self.age, 'years old.')


# Python 中所有的类都继承自 object 类，Python支持多继承
class Student(Person):
    def __init__(self, name, age, stu_no):
        super(Student, self).__init__(name, age)
        self.stu_no = stu_no


stu = Student('张三', 20, 1001)
stu.hello()


class Teacher(Person):
    def __init__(self, name, age, work_year):
        super(Teacher, self).__init__(name, age)
        self.work_year = work_year

    # 方法覆盖
    def hello(self):
        print('my name is ', self.name, ", i'am ", self.age, 'years old, ', 'already worked ', self.work_year, 'years.')


tea = Teacher('李四', 34, 4)
tea.hello()
