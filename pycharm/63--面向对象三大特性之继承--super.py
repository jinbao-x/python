#  重写了父亲的赚钱方法，靠写代码赚钱，但是写了一半发现还是经商赚钱，想再次调用父亲的方法赚钱该怎么调用父亲的方法呢？
class Father():
    def __init__(self):
        self.__hobby = '抽烟'  # 这个私有属性不希望子类继承

    def take_money(self):
        print('经商赚钱')


class Son(Father):
    def take_money(self):  # 重写父类的方法
        print('写代码赚钱')

        super().take_money()  # 使用super()调用父亲的方法，加上.take_money相当于调用父亲的赚钱方法


lisi = Son()
lisi.take_money()  # 可以看到这里的结果还是经商

# 继承
# 1、继承具有传递性，不管有多少层继承，都会往上继承
# 2、当父类的方法满足不了子类的话，子类可以重写继承
# 3、当子类重写了方法，但是后来忽然又发现还是需要使用一下父类的方法，可以使用super()调用父类的方法
# 4、如果父类有一些属性或者方法不希望子类调用，那么可以使用私有属性或方法
