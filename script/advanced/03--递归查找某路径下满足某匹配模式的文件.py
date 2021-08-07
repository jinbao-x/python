#!/usr/bin/python
import os
import fnmatch


def is_file_match(filename, patterns):  # 抽象出来一个判断文件是否满足某个匹配模式的方法
    for pattern in patterns:  # 遍历patterns，如果某个满足匹配模式返回True，不满足则返回False
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def find_specific_file(root, patterns=['*'], exclude_dirs=[]):  # 定义三个参数，分别是查找文件的根路径，匹配模式，排除的目录
    # 匹配模式和排除的目录均使用列表的形式
    for root, dirnames, filenames in os.walk(root):  # 在这个根路径下边使用os.walk遍历所有内容，以三个对象形式返回
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)
                # yield是生成器的一种写法，相当于是保存了这个查找的算法，不同的目录结构，文件个数和内容都会不一样
                # 这样就不必先初始化一个列表，然后往列表里存数据，最后在访问列表，用了yield直接在每次循环的时候每匹配一次就返回一次结果

        for dirname in exclude_dirs:  # 遍历"排除目录"的列表
            if dirname in dirnames:
                dirnames.remove(dirname)


for file in find_specific_file(os.getcwd(), patterns=['01*']):  # 这里传入的是当前路径os.getcwd()
    print(file)
