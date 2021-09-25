#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 22:42
# @Author  : zengxt
# @File    : 06_if_statement.py

'''
    90-100 A级
    80-89 B级
    70-79 C级
    60-69 D级
    0-59 E级
'''
score = int(input('请输入一个成绩：'))

if 90 <= score <= 100:
    print('A级')
elif 80 <= score <= 89:
    print('B级')
elif 70 <= score <= 79:
    print('C级')
elif 60 <= score <= 69:
    print('D级')
elif 0 <= score <= 59:
    print('不及格')
else:
    print('对不起，成绩有误！')

# 条件表达式
num_a = 10
num_b = 20
'''
if num_a >= num_b:
    print(num_a, '>=', num_b)
else:
    print(num_a, '<', num_b)
'''
# 条件表达式：if 条件为 True 取前面的值，否则取 else 的值
print((str(num_a) + '>=' + str(num_b)) if num_a >= num_b else (str(num_a) + '<' + str(num_b)))
