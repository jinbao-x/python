import os
import fnmatch


class FileFind(object):
    rules = ['*']
    matches_dir = []
    matches_file = []

    @staticmethod
    def get_all(exclude_dir=''):
        for root, dirnames, filenames in os.walk(os.getcwd()):  # 使用os.walk方法，默认传入当前路径
            for extensions in FileFind.rules:
                if exclude_dir in dirnames:
                    dirnames.remove(exclude_dir)
                for filename in fnmatch.filter(filenames, extensions):
                    FileFind.matches_dir.append(os.path.join(root, filename))
                for dirname in fnmatch.filter(dirnames, extensions):
                    FileFind.matches_file.append(os.path.join(root, dirname))

        return FileFind.matches_file, FileFind.matches_dir  # 以列表形式返回


my = FileFind()
print(my.get_all('.idea'))  # 以参数的形式传入要排除遍历的目录，如果没写参数，默认不排除
