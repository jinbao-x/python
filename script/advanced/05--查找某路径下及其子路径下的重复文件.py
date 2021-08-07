import os
import fnmatch
import hashlib


class FileFind(object):
    CHUNK_SIZE = 8192  # 定义类属性，定义检测文件内容md5值的字节数

    @staticmethod
    def get_chunk(filename):  # 定义一个获取文件的CHUNK_SIZE字节内容的方法，返回迭代对象，这样避免md5校验时直接update整个文件会卡住
        # 也避免按行update文件内容速度过慢
        with open(filename) as f:
            while True:
                chunk = f.read(FileFind.CHUNK_SIZE)
                if not chunk:
                    break
                else:
                    yield chunk

    @staticmethod
    def get_file_checksum(filename):  # 定义获取md5校验值的方法
        h = hashlib.md5()
        for part in FileFind.get_chunk(filename):
            h.update(part.encode("utf8"))
        return h.hexdigest()

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

    @staticmethod  # 写一个静态方法，遍历目录及其子目录下的所有文件，并返回文件路径
    def get_all(patterns=['*'], exclude_dirs=[]):  # 匹配模式默认为全部，当然也用列表的形式写多个匹配模式传入，排除目录为默认无
        for root, dirnames, filenames in os.walk(os.getcwd()):  # 使用os.walk方法
            FileFind.exclude_remove(dirnames, exclude_dirs)  # 调用exclude_remove方法，直接把dirnames列表中在排除清单里的目录删掉
            for filename in filenames:
                if FileFind.is_file_match(filename, patterns):
                    yield os.path.join(root, filename)

    @staticmethod
    def get_same_file():  # 定义一个查找相同文件的方法，遍历一下使用get_all得到的文件路径(可迭代对象)，在遍历过程中，判断文件的校验值是否在字典中
        # 如果不在字典中，则加入字典，如果存在于字典中，则打印出该文件的绝对路径，这样即可判断出来md5值一样的文件
        record = {}  # 因为散列值是唯一的，可以把散列值当做键，文件名当做值
        for item in FileFind.get_all():  # 遍历get_all方法，获取所有文件路径，并获取md5值，与字典里的作比较
            checksum = FileFind.get_file_checksum(item)
            if checksum in record:  # 判断这个文件的md5值是否在字典中
                print('找到重复的文件：{0} 和 {1} 重复了'.format(record[checksum], item))
            else:
                record[checksum] = item


if __name__ == '__main__':
    my = FileFind()
    my.get_same_file()
