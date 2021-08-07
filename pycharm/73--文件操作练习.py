# 在当前路径下创建一个test文件夹
# 进入到test文件夹下批量创建几个测试文件：01--test.py、02--test.py...创建许多个
# 打印出test目录下的文件
# 批量重命名文件，将刚刚创建的文件对应修改为：01.py、02.py...
# 打印出test目录下的文件

# 编辑01--test.py文件，追加几行内容，内容为本文件里的前三行注释，并打印出01--test.py文件里的内容
# 删除02--test.py文件，并打印出当前路径(test)下的所有文件
# 重命名03--test.py文件，命名为ceshi.py，并打印出当前路径下的所有文件
# 退出test目录，并删除掉test文件夹

import os


class FileOperation():  # 写一个批量重命名的类
    def __init__(self, path):
        self.original_dir = path  # 初始化一个属性，用来存放原始目录，也就是本脚本所处的目录

    # 写一个方法用来创建工作目录
    def mkdir_test(self, work_dir='test'):  # 在原始目录创建一个test目录，当做工作目录，也可以接收参数创建一个其他名字的目录
        os.chdir(self.original_dir)  # 先切到原始目录
        if not os.path.isdir(work_dir):  # 先判断工作目录是否存在，不存在则创建
            os.mkdir(work_dir)

    # 写一个批量创建许多文件的方法
    def file_touch_many(self, number, middle='test', tail='py', work_dir='test'):
        # 批量创建文件，传入四个参数，第一个是文件个数(必需)，第二个是名字，第三个是尾缀,最后一个参数是工作目录(默认为test)
        os.chdir(self.original_dir)
        os.chdir(work_dir)
        for i in range(1, number + 1):
            tmp = '.'.join(('--'.join((str(i), middle)), tail))  # 将传入的参数拼接起来
            with open(tmp, 'w') as f:  # open打开文件，如果没有则创建
                pass

    def file_rename_many(self, work_dir='test'):
        os.chdir(self.original_dir)
        os.chdir(work_dir)
        for item in os.listdir():
            tmp = item.rsplit('--')  # 以--拆开
            new_name = tmp[0] + '.py'
            os.rename(item, new_name)

    def file_show(self, work_dir='test'):  # 传入参数为工作目录，默认为test
        os.chdir(self.original_dir)
        os.chdir(work_dir)
        return os.listdir()


if __name__ == '__main__':
    my = FileOperation(os.getcwd())  # 创建对象，创建时传入参数，也就是本脚本所在目录
    my.mkdir_test()
    my.file_touch_many(5)
    print(my.file_show())
    my.file_rename_many()
    print(my.file_show())
