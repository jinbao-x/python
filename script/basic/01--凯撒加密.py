#!/usr/bin/python2
# -*- coding: UTF-8 -*-
#脚本功能：字符串加密，凯撒加密，练习字符串处理函数ord以及chr
#脚本思路：从交互式输入中获取字符串，再进行相应处理获得一个加密后的字符串
#使用方法：加权限./执行，或直接调用python执行（python2 xxx.py或python3 xxx.py）
#使用环境：linux系统中练习
#from __future__ import print_function
code = raw_input("请输入明文：")
for i in code:
    if ord("a") <= ord(i) <= ord("z"):
        print(chr(ord("a") + (ord(i) - ord("a") + 3)%26),end='')
    else:
        print(i,end='')

