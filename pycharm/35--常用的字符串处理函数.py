# 统计字符出现次数
s = 'zhangsan'
print(s.count('a'))

# 替换字符
print(s.replace('a', 'f', 1))  # 第三位是替换次数

# split分割字符串
print(s.split('a'))

# 判断是否以某字母开头
print(s.startswith('z'))

# 去掉左右两侧的空格以及换行
s = ' wangwu\n'
print(s)
print(s.strip())  # 去掉两边的空格或换行
print(s.rstrip())  # 去掉右边的...
print(s.lstrip())  # 去掉左边的...

# 拼接字符串
s1 = 'lisi'
s2 = 'maliu'
print(s1 + s2)
print(s1.join(s2))  # 此种方法相当于把s2拆开，然后将s1字符穿穿插进去

# 查找字符
s = 'zhangsan'
print(s.find('a'))  # 返回字符索引，默认从左边开始查，以0开始，如果不存在返回-1
print(s.rfind('a'))  # 返回字符索引，从右边开始查
print(s.index('a'))  # 返回字符索引值，如果不存在报错
