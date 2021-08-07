import os
import fnmatch


class FileFind(object):
    rules = ['*']
    matches_dir = []
    matches_file = []

    @staticmethod
    def get_cur_dir():
        return os.getcwd()  # 获取当前路径，在哪里运行python脚本，就在哪里遍历目录树

    @staticmethod
    def get_all():
        for root, dirnames, filenames in os.walk(FileFind.get_cur_dir()):  # 使用os.walk方法
            for extensions in FileFind.rules:
                for filename in fnmatch.filter(filenames, extensions):
                    FileFind.matches_dir.append(os.path.join(root, filename))
                for dirname in fnmatch.filter(dirnames, extensions):
                    FileFind.matches_file.append(os.path.join(root, dirname))
        return FileFind.matches_file, FileFind.matches_dir  # 以列表形式返回


my = FileFind()
print(my.get_all())
