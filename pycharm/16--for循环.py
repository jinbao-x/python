# 面向数字范围的循环
for i in range(5):  # 不包括5，也就是说用range一定要记得往后多延伸一位
    print(i)
for i in range(1, 10, 2):  # 第三个数代表步长
    print(i)

# 面向文件内容的循环
f1 = open("01--类型转换.py")
for line in f1:
    print(line, end='')  # 因为文件里边每行内容末尾本身就有换行了，所以print每行内容的时候如果没有end=''则会多出来一行空
f1.close()

# 面向字符串的循环
for s in "LongLongStr":
    print(s)

# 面向列表list的循环
ls = ["My ", "name ", "is ", "xu", "jin", "bao ", 666]
for item in ls:
    print(item, end='')     # 去掉换行，这样就能将这些字符串在一行连着显示了
