class Father():
    def __init__(self):
        self.__hobby = '抽烟'  # 这个私有属性不希望子类继承

    def __snore(self):  # 定义私有方法，这个行为不希望子类继承
        print('打呼噜')

    @classmethod
    def __swimming(cls):  # 定义私有类方法，可以在函数体内在子类中调用，但是子类不可以继承私有类方法
        print('私有类方法')

    @staticmethod
    def __disaster():  # 定义一个私有的静态方法(和对象本身没有引用关系)，该私有静态方法，子类也不可继承
        print('天灾人祸')

    def take_money(self):
        print('经商赚钱')


class Son(Father):
    def take_money(self):  # 重写父类的方法
        print('写代码赚钱')

        super().take_money()  # 写代码发现不咋赚钱，然后使用super()调用父亲的方法


lisi = Son()
lisi.take_money()  # 可以看到这里的结果还是经商
# lisi.__snore      # 这里可以发现子类没办法调用这个打呼噜方法


# 记住一点，为什么叫私有？为什么有私有属性、私有方法、私有类方法、私有静态方法这些概念？
# 这意味着这个私有的东西，只有类里能用，外部是不能用的，外部如果想调用修改之类的，都需要在内部写一个公有的方法，在公有方法里进行对私有内容的修改
# 而且私有的东西，子类是不能继承的！
