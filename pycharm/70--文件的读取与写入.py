f = open('01--类型转换.py', 'r')  # 注意open函数里是要写文件的绝对路径，不能只写文件名
print(f.read())  # .read()方法读取文件所有内容
f.close()

f1 = open('00--test.py', 'a+')  # a+支持读写，不存在则会创建，与w+区别在于覆盖还是不覆盖
f1.write('# 啥\n# 好简单\n# 就这？\n')
f1.close()

f2 = open('00--test.py', 'r')
print(f2.read())  # read()是读所有，括号里写数字可以只读入指定个数的字符
f2.close()

f3 = open('00--test.py', 'r')
print(f3.readline())  # 读一行
f3.close()

f4 = open('00--test.py', 'r')
print(f4.readlines())  # 读所有行，以列表形式保存
f4.close()

# f5 = open('00--photo.png', 'wb')  # wb二进制写，所以写的时候内容需要是流
# f5.write(bytes('zifuchuan', encodings='utf8'))    # 因为只二进制文件，所以这里可以使用字符串再转一下字节就可以测试了
# f5.close()

# 更加推荐使用python中的上下文管理器，这样可以不用在末尾考虑.close关闭问题
with open('00--test1.py') as f5:
    print(f.read())
