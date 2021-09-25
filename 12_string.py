#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/10 20:49
# @Author  : zengxt
# @File    : 12_string.py

# 字符串驻留机制：仅保留一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，
# Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
str1 = 'python'
str2 = "python"
str3 = '''python'''
# 内存地址相同
print(str1, id(str1))
print(str2, id(str2))
print(str3, id(str3))

# python 字符串拼接 join 方法比 + 效率高
print('abc' + 'def')
print(''.join(('abc', 'def')))


print('====================================字符串查找操作======================================')
print('pythonpy'.index('y'))  # 查找子串第一次出现的位置，如果找不到，则抛出 ValueError
print('pythonpy'.rindex('y'))  # rindex查找子串最后一次出现的位置
# print('pythonpy'.index('yy')) # ValueError: substring not found

print('pythonpy'.find('y'))  # 查找子串第一次出现的位置，如果找不到，则返回-1
print('pythonpy'.rfind('y'))  # rfind查找子串最后一次出现的位置
print('pythonpy'.find('yy'))


# 字符串的所有操作都会产生新的字符串
print('====================================字符串大小写转化======================================')
print('hello, python'.upper())  # 字符串的所有字符都大写
print('heLLO, pyTHon'.lower())  # 字符串的所有字符都小写
print('heLLO, pyTHon'.swapcase())  # 字符串中原来大写的转换成小写，原来小写的转换成大写
print('heLLO, pyTHon'.capitalize())  # 把第一个字符转换成大小，把其余的字符转换成小写
print('heLLO, pyTHon'.title())  # 把每个单词的第一个字符转化成大写，把每个单词剩余的字符转换成小写


print('====================================字符串内容对齐操作======================================')
str4 = 'hello, python'
print(str4.center(20, '*'))  # 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，默认是空格，如果设置宽度小于实际宽度则返回原字符串
print(str4.ljust(20, '*'))  # 左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，默认是空格，如果设置宽度小于实际宽度则返回原字符串
print(str4.rjust(20, '*'))  # 右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数可选，默认是空格，如果设置宽度小于实际宽度则返回原字符串
print(str4.rjust(20))
print(str4.rjust(10))
print(str4.zfill(10))  # 右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
print(str4.zfill(20))
print('100'.zfill(8))
print('-100'.zfill(8))  # 填充的0放在 - 后面


print('====================================字符串的分隔操作======================================')
# split() 函数从字符串的左边开始分隔，默认使用空格分隔，返回的值是一个列表
# 通过参数sep指定分隔符，通过参数maxsplit指定分隔字符串时的最大分隔次数，在经过最大次分隔之后，剩余的子串会单独作为一部分
print('hello python'.split())
print('hello|python|world'.split(sep='|'))
print('hello|python|world'.split(sep='|', maxsplit=1))

# rsplit() 方法从右边开始分隔
print('hello python'.rsplit())
print('hello|python|world'.rsplit(sep='|'))
print('hello|python|world'.rsplit(sep='|', maxsplit=1))


print('====================================字符串的操作方法======================================')
# isidentifier：判断指定的字符串是不是合法的标识符
print('1、是否是合法标识符：', 'hell,p'.isidentifier())  # False
print('2、是否是合法标识符：', 'hellp'.isidentifier())  # True

# isspace：判断指定的字符串是否全部由空白字符组成（回车、换行、水平制表符）
print('3、是否全部是空格：', '\t\r\n'.isspace())  # True

# isalpha：判断指定的字符串是否全部由字母组成
print('4、是否全部由字母组成：', 'abc'.isalpha())  # True
print('5、是否全部由字母组成：', 'abc四'.isalpha())  # True
print('6、是否全部由字母组成：', 'abc1'.isalpha())  # False

# isdecimal：判断指定字符串是否全部由十进制的数字组成
print('7、是否全部是十进制数字：', '133'.isdecimal())  # True
print('8、是否全部是十进制数字：', '133a'.isdecimal())  # False
print('9、是否全部是十进制数字：', '四'.isdecimal())  # False
print('10、是否全部是十进制数字：', 'ⅠⅡⅢ'.isdecimal())  # False

# isnumeric：判断指定的字符串是否全部由数字组成
print('11、是否全部是数字：', '133'.isnumeric())  # True
print('12、是否全部是数字：', '133a'.isnumeric())  # False
print('13、是否全部是数字：', '四'.isnumeric())  # True
print('14、是否全部是数字：', 'ⅠⅡⅢ'.isnumeric())  # True

# isalnum：判断指定的字符串是否全部由字母和数字组成
print('15、是否全部是字母和数字：', '123a'.isalnum())  # True
print('16、是否全部是字母和数字：', 'ⅠⅡⅢ'.isalnum())  # True
print('17、是否全部是字母和数字：', 'as无'.isalnum())  # True
print('18、是否全部是字母和数字：', 'as无，'.isalnum())  # False


print('====================================字符串的替换与合并======================================')
# replace() 方法，字符串替换，第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后的得到的字符串
# 替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
print('hello, python, python, python'.replace('python', 'java'))
print('hello, python, python, python'.replace('python', 'java', 2))  # 默认会全部替换

# join() 方法，将列表或元组的字符串合并成一个字符串
lst = ['python', 'java', 'C++']
print('&'.join(lst))
print(''.join(lst))
print('@'.join('python'))


print('====================================字符串的比较======================================')
# 1、比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，
# 直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
# 2、比较原理：两个字符进行比较时，比较的是其ordinal value（原始值），调用内置函数 ord 可以得到指定字符的原始值
# 与内置函数ord对应的是内置函数chr，调用内置函数 chr 时指定的 ordinal value可以得到其对应的字符
print(ord('a'))  # ascii 编码
print(chr(97))
print(chr(98))
print(ord('曾'))
print(chr(26366))

print('apple' > 'app')  # True
print('apple' > 'bpp')  # False

s1 = 'apple'
s2 = 'apple'
print(s1 == s2)  # True, == 比较的是字符串的值
print(s1 is s2)  # True, is 比较的是字符串的地址


print('====================================字符串的格式化======================================')
# 三种方法
print('我的名字叫%s, 今年%d岁了！' % ('张三', 34))
print('我的名字叫{0}, 今年{1}岁了！'.format('张三', 34))
name = '张三'
age = 34
print(f'我的名字叫{name}, 今年{age}岁了！')

print('%10d' % 90)
print('%.3f' % 3.1415926)
print('%10.3f' % 3.1415926)


print('====================================字符串的编码与解码======================================')
s3 = '床前明月光'
print(s3.encode(encoding='GBK'))  # GBK 编码格式，一个汉字占两个字节
print(s3.encode(encoding='UTF-8'))  # UTF-8 编码格式，一个汉字占三个字节

# 解码与编码需要使用相同的编码格式，否则会报错
print(s3.encode(encoding='GBK').decode(encoding='GBK'))
print(s3.encode(encoding='UTF-8').decode(encoding='UTF-8'))
