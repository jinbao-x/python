class Dog():
    def __init__(self):
        self.name = '狼狗'
        self.__age = 12  # 加俩下划线__变成私有属性，私有属性在函数外是用不了的

    def show_age(self):
        print(self.__age)


kitty = Dog()
kitty.name = '哈士奇'  # 这里定义共有属性
kitty.__age = 13  # 这里定义共有属性
print(kitty.name)
kitty.show_age()  # 可以看到上面kitty.__age那个赋值其实并没有给属性赋值
print(kitty.__age)  # 这里是打印公有属性，这里容易引起迷惑，所以公有属性


# 既然专门定义了私有属性，而私有属性在外面改不了也调用不了，那么需要用其他方法修改和调用
class Cat():
    def __init__(self):
        self.name = 'mimi'
        self.__age = 7

    # 利用公有方法(也就是这个方法在函数外是可以用的)，给私有属性赋值
    def set_age(self, age):  # 这里加个age参数，因为要修改年龄，因此需要在调用此方法的时候能传参进来
        self.__age = age

    def get_age(self):
        return self.__age


xiaohong = Cat()
xiaohong.set_age(23)  # 这里调用公有方法，然后修改函数内的私有属性
print('xiaohong的年龄是{}'.format(xiaohong.get_age()))  # 获取函数内的私有属性


# 为什么要设计这么一个私有属性呢？用来干什么呢？
# 因为公有属性在函数体外也可以随便赋值，这可能导致会赋值一个完全错误的值
# 有了私有属性，在函数体外修改不了，可以写一个公有方法，并且在这个方法里加判断才做赋值操作，这就防止赋一个错误的值
# 除此之外，私有属性还可以避免子类直接访问和名字冲突的问题

class Person():
    def __init__(self, nationality='China', complexion='yellow'):
        self.nationality = nationality
        self.__complexion = complexion

    def get_all(self):  # 获取该对象的所有属性
        for i, j in vars(self).items():
            print(i, j)

    def set_complexion(self, complexion):  # 设置一个公有方法更改私有属性
        self.__complexion = complexion

    def get_complexion(self):  # 设置一个公有方法查询私有属性
        return self.__complexion


zhangsan = Person()
zhangsan.get_all()
print(zhangsan.get_complexion())  # 因为是返回值，需要print一下
