#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 23:27
# @Author  : zengxt
# @File    : 07_for_while_statement.py

# range 函数，有三个参数 start(包含)、stop(不包含)、step
# 注意：不管range序列的长度有多长，它在内存中占用的空间都是相同的，因为仅仅需要存储start、stop和step，只有当用到range对象时，才会去计算序列的值
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 只指定末尾值，从0开始，步长为1
print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9] 指定起始值和结束值，步长为1
print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9] 指定起始值、结束值、步长

# in 操作符可以判断 在字符串中是否存在，在列表中是否存在
print(9 in range(10))
print(10 in range(10))

# 计算 1-100 之间的偶数和
index = 1
total = 0
while index <= 100:
    total += index if not (index % 2) else 0
    index += 1
print(total)

# for in 循环
for item in 'Python':
    print(item)

for num in range(1, 11):
    print(num)

# 打印 100-999之间的水仙花数
for num in range(100, 1000):
    ge = num % 10
    shi = num // 10 % 10
    bai = num // 100
    if (ge ** 3 + shi ** 3 + bai ** 3) == num:
        print('水仙花数：', num)

# else 也能和 for 及 while 搭配使用，当循环不是由break退出时会执行else
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起三次密码均输入错误！')
