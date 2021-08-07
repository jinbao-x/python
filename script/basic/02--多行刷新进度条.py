#!/usr/bin/python2
# -*- coding: UTF-8 -*-
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a, b = '**' * i,'..' * (scale - i)
    c = (i*100)/10
    print("{:^3.0f}%[{}->{}]" .format (c, a, b))
    time.sleep(0.1)
print("------执行结束------")
#整体循环21次，从0循环到21
