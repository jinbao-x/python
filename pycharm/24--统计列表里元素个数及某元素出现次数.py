ls = [23, 56, 23, 8, 23, 90, 45, 13]

# 获取列表元素个数，也就是列表长度
print(len(ls))  # 获取列表里元素个数
print(ls.count(23))  # 或取23这个元素出现的次数

# 判断某元素是否是在列表里，返回布尔值
print(2 not in ls)
print(23 in ls)

# 遍历列表里的元素
for i in ls:
    print(i)
