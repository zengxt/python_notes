#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 20:20
# @Author  : zengxt
# @File    : 03_input.py

while True:
    name = input('你的名字是：')
    print(name, type(name))

    if name == 'exit':
        break
