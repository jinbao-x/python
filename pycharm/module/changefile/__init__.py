# from . import readfile  # 先在init里导入一下模块，先初始化一下，然后，包之外的另外一个文件就可以使用from 包 imoprt *来调用了
# from . import writefile

# __init__
# 1、声明文件夹是个包
# 2、可以做初始化操作
# 3、可以声明__all__影响 from 包 import *导入，在__all__里写的才会导入


# 当然这个init文件也可以想其他普通模块文件内一样，可以使用__all__ = ['readfile']这样的方式来确认模块里的哪些方法可以使用
# 这种是为了解决其他模块文件里用from changefile import *这种星花的导入方式，避免其他模块文件里用星花的方式引用了init里指定的模块的所有的方法
