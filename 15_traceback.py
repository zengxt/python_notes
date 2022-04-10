#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 19:59
# @Author  : zengxt
# @File    : 15_traceback.py

import traceback

try:
    print('----------------------')
    print(10 / 0)
except ZeroDivisionError:
    traceback.print_exc()
