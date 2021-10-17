#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 23:23
# @Author  : zengxt
# @File    : 02_import.py
import cacl
import package01.module01 as pm
# import 方式导入，只能导入包，或者模块

print(cacl.add(10, 20))

print(pm.name)

# from ... import ... 方式可以导入 模块，变量，函数，类等
# from package01.module01 import name
# from cacl import add
