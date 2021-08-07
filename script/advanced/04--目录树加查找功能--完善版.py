import os
import fnmatch


class FileFind(object):
    @staticmethod
    def is_file_match(filename, patterns):  # 判断文件或目录是否满足某个匹配模式，传入两个参数：文件名，匹配模式，这两个参数均是列表形式
        for pattern in patterns:  # 遍历这些匹配模式
            if fnmatch.fnmatch(filename, pattern):  # 如果满足匹配模式，则返回真
                return True
        return False  # 默认返回非真

    @staticmethod
    def exclude_remove(dirnames, exclude_dirs):  # 抽象出来一个方法，传入两个参数，第一个是所有目录清单，第二个是排除清单
        for exclude_dir in exclude_dirs:
            if exclude_dir in dirnames:
                dirnames.remove(exclude_dir)

    @staticmethod
    def get_all(patterns=['*'], exclude_dirs=[]):  # 匹配模式默认为全部，当然也用列表的形式写多个匹配模式传入，排除目录为默认无
        for root, dirnames, filenames in os.walk(os.getcwd()):  # 使用os.walk方法
            FileFind.exclude_remove(dirnames, exclude_dirs)  # 调用exclude_remove方法，直接把dirnames列表中在排除清单里的目录删掉
            for filename in filenames:
                if FileFind.is_file_match(filename, patterns):
                    yield os.path.join(root, filename)


if __name__ == '__main__':
    my = FileFind()
    # for file in my.get_all():
    #     print(file)

    for file in my.get_all(patterns=['*'], exclude_dirs=['.idea']):
        print(file)

    print('-----------------')  # 分隔符

    for file in my.get_all(patterns=['01*']):
        print(file)
