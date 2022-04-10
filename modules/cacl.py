#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 23:21
# @Author  : zengxt
# @File    : cacl.py


def add(a, b):
    return a + b


# __name__记录模块名称的变量，表示只有当运行本程序时，才会执行，被其他模块import时不会执行
if __name__ == '__main__':
    print(add(20, 30))
