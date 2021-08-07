class MyException(Exception):  # 定义一个类，继承Exception
    def __init__(self, name):
        self.name = name  # 为这个类定义一个name类属性，方便初始化实例的时候可以直接调用该类属性


def test():  # 定义一个函数
    name = input('请输入一个名字')  # 从输入中捕获异常
    try:
        if name == 'zhangsan':
            raise MyException(name)  # 抛出异常！！！
        # 为什么要这么做呢？是因为正常情况下输入任何的东西，对于此程序来说在这里都不算是错误的，但是呢，我想把用户的某些输入"当做"异常，然后再执行相应的异常报错
    except MyException as e:  # 因为上面是自定义抛出的MyException异常，所以这里捕获MyException
        print('您输入的是{}，所以报错了'.format(e.name))  # name传入到类里做了属性，所以这里可以使用e.name表示用户输入


test()  # 调用test函数
