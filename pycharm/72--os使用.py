import os

# 注意以下所有方法里的文件参数，都应该是写路径的，因为有的使用的是相对路径，所以看起来像是只写了文件名

# 重命名
# os.rename('00--test1.py', '00--test2.py')

# 删除文件
# os.remove('xxx/00--test2.py')

# 创建文件夹
# os.mkdir('test')

# 删除文件夹
# os.rmdir('xxx/test')

# 获取当前路径
print(os.getcwd())

# 改变当前路径
# os.chdir('../')   # 往上退一层

# 获取某个路径下的所有文件
print(os.listdir('./'))  # 使用./获取当前路径下的所有文件
