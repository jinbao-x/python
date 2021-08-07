#!/usr/bin/python3
# -*- coding: UTF-8 -*-     #chinese characters
from __future__ import print_function   #end=''
import time
num = 100
scale = 10
print("----------执行开始----------")
for i in range(num):
    c = i // scale
    time.sleep(0.01)
    a = '**' * c
    b = '..' * (9 - c)
    print("\r{:^3.0f}%[{}->{}]".format(i,a,b),end='')
print("")
print("----------执行结束----------")

