#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 13:41
# @Author  : zengxt
# @File    : 08_list.py

print('======================== list 的 index 和 count 函数 =================================')
mylist = ['hello', 'world', 34, 56, 'hello', 'python', 34.56]
print(mylist.index('hello'))  # 查找list中的第一个元素下标，没有的话错误
print(mylist.count('hello'))  # 2 元素在list中出现的次数
print(mylist.count(100))  # 0


print('======================= list 的 切片操作 ==============================================')
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# 列表的切片操作  start : stop : step
print('list2[1:6:1] = ', list2[1:6:1])
print('list2[1:6:2] = ', list2[1:6:2])
print('list2[:6:2] = ', list2[:6:2])  # start 默认为 0
print('list2[::2] = ', list2[::2])  # stop 默认为 列表长度
print('list2[::] = ', list2[::])  # step 默认为 1

print('list2[::-1]', list2[::-1])  # 如果 step 为负数，start默认为列表长度， stop默认为 0
print('list2[8:4:-1]', list2[8:4:-1])


print('======================= 判断元素在列表中是否存在 ========================================')
print(10 in list2)
print(100 in list2)

# 遍历 list
for item in list2:
    print(item, end='\t')
print()


print('======================= list 中添加元素 ==================================================')
list3 = [12, 20, 30]
print(list3, id(list3))
list3.append('hello')
print(list3, id(list3))

temp = ['200', 300]
list4 = [100]
list4.append(temp)  # append 将列表作为一个元素添加到当前列表的末尾
print(list4)

list4 = [100]
list4.extend(temp)  # extend 至少向列表中添加一个元素，将入参的list分解成一个个的元素
print(list4)

# insert 可以在任意位置插入一个元素
list4.insert(2, 1000)
print(list4)

# 把切片的部分整体替换
list4[1:] = [111]
print(list4)


print('================================== 删除 list 中的元素 ===================================')
list5 = [10, 20, 30, 40, 20]
list5.remove(20)  # remove 按元素值删除，如果存在重复元素，值删除第一个
print(list5)
# list5.remove(100) # list.remove(x): x not in list

list5.pop(3)
print(list5)  # pop 按元素的索引删除元素
list5.pop()  # 删除最后一个元素
print(list5)
# list5.pop(3) # pop index out of range

# 切片操作，删除不止一个元素
lst = [1, 2, 3, 4, 5, 6, 7]
lst[2:4] = []
print(lst)

# 清空list
lst.clear()
print(lst)

# del 语句直接删除变量
del lst
# print(lst) # NameError: name 'lst' is not defined


print('================================== 修改 list 中的元素 ===================================')
list6 = ['hello', 'python', 200]
list6[1] = 100
print(list6)
list6[1:] = ['world', 'hahaha']
print(list6)


print('================================== list 排序 ============================================')
list8 = [12, -10, 54, 99, 5, 23]
print('排序前的list = ', list8, id(list8))
list8.sort()
print('排序后的list = ', list8, id(list8))
list8.sort(reverse=True)
print('降序排序后的list = ', list8, id(list8))

# 内置函数sorted()生成一个新的list，而sort是对原list进行排序， 两个函数的reverse参数一样
list9 = [12, -10, 54, 99, 5, 23]
new_list = sorted(list9)
print(list9)
print(new_list)


print('================================== 列表生成式 ============================================')
list10 = [i * i for i in range(1, 11)]
print(list10)
