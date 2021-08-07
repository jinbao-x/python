class Person(object):  # 父类==基类
    def __init__(self):
        self.name = '人类'


class athletes(Person):  # 继承Person，子类==派生类
    # def __init__(self):  # 注意这种用法是错误的，父类(基类)已经有初始化方法了，现在再写一个初始化方法就相当于初始化方法的重写
    #     self.age = 23     # 但是父类初始化方法里有一些属性这里是没有重写的，这就会导致冲突，因此可以采用下面方法
    def __init__(self):
        super().__init__()  # 在子类的初始化方法里用super()调用父类的初始化来完成父类已有的属性初始化
        self.age = 23  # 子类特有的属性则单独有子类进行初始化，这样就避免了冲突

    def exercise(self):
        print('训练')


class male_athlete(athletes):
    def exercise(self):  # 重写exercise方法
        print('锻炼举重')


class sportswomen(athletes):
    def exercise(self):
        print('锻炼瑜伽')


zhangsan = male_athlete()
zhangsan.exercise()  # 发现调用的是子类的方法，这是因为子类重写了父类里的相同方法


class Father():
    def take_money(self):
        print('经商赚钱')


class Son(Father):
    def take_money(self):  # 重写父类的方法
        print('写代码赚钱')


lisi = Son()
lisi.take_money()

# 继承
# 1、继承具有传递性，不管有多少层继承，都会往上继承
# 2、当父类的方法满足不了子类的话，子类可以重写继承
