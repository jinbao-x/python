# __all__ = ['add', 'jian']
#
# from tools import *

# from tools import add  # 从文件tools中导入add函数
# from tools import *  # 尽量不要用这种方法，如果模块中有重复的函数名字，后面导入的会覆盖前边导入的
# import tools  # 这种直接导入模块，那么后边使用这个模块里的函数的时候就需要用模块.的方式调用
# from tools import Tool  # 导入类，调用的用法跟在一个文件内操作基本一样

# from changefile.readfile import read  # 导入包里的某个模块里的某个方法
# from changefile import readfile, writefile  # 导入包里的某个模块
# 也就是说正常情况下，至少确定到导入哪个模块

# from changefile import *
# import changefile # 导入包
# 上面这两中方法直接这么使用是不可以的，不过可以在__init__文件内先把模块导入一下
# 因为__init__.py文件内的导入操作是初始化操作，不需要调用就会执行的，且因为init里已经导入了确切的模块，所以调用这个包时，就知道有哪些模块是可以被引用的
# 说白了，不能不指定使用包里的哪些模块，只有指定了模块，才可以在包外调用

if __name__ == '__main__':
    # 当自己运行的时候，返回的值是__main__，这意味着这个判断相等，所以在本文件内运行的时候可以执行下面的程序，避免模块被调用的时候，二次加载
    # 当被当做模块调用的时候，返回的是模块的名字
    from tools import add

    result = add(7, 8)
    print(result)
