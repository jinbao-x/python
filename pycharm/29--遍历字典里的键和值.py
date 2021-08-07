d = {'id': 1, 'name': 'tom', '性别': '男', '手机': 13456778988}

# 遍历键
for i in d.keys():
    print(i)

# 遍历键，不指定keys默认就是遍历键
for i in d:
    print(i)

# 遍历值
for i in d.values():
    print(i)

# 遍历键值对，这个返回元组的形式
for i in d.items():
    print(i)

# 一般情况这么使用
for i, j in d.items():
    print(i, j)

# 判断键在不在字典里
print('name' in d)  # 判断name这个键在不在d字典里

# 补充：
# 能够当做字典的键：字符串、整数、浮点数、布尔、元组
# 不能够当做字典的键：列表、字典
# 也就是可变类型的数据不能当做字典的键
