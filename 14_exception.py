#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 23:09
# @Author  : zengxt
# @File    : 14_exception.py

try:
    num1 = int(input('请输入第一个数字：'))
    num2 = int(input('请输入第二个数字：'))
    result = num1 / num2
    print('结果为', result)
except ZeroDivisionError:
    print('除数不能为 0 ')
except ValueError:
    print('请输入一个正确的数字。')
except BaseException as e:
    print(e)
else:
    print('except 和 else 只会执行一个。')
finally:
    print('无论是否出现异常，finally里的代码都会执行。')
print('程序结束！！')

# try except else：异常了执行 except 块，没有异常执行else

# try except else finally：不管异常与否，finally 中的代码都是执行，通常用来释放资源
