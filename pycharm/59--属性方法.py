class Person():
    def __init__(self):
        self.__age = 0  # 这里定义了一个私有属性

    def set_age(self, age):  # 这里写了一个公有方法set_age用来给私有属性__age赋值
        if age > 0:
            self.__age = age
        elif age < 0:
            print('age赋值超出范围')

    def get_age(self):  # 通过写一个公有方法get_age获取私有属性__age
        return self.__age


zhangsan = Person()
zhangsan.set_age(10)  # 这里你会发现，需要专门用一个公有方法set_age()才能完成对私有属性的设置，但是如果我还想用属性赋值的那种方法在外部给私有属性赋值呢？
print(zhangsan.get_age())  # 这里你会发现，还需要一个专门的公有方法get_age()完成私有属性的访问，但是我想让对于这个私有属性的两个操作用一个属性方法就能实现，且看下面的属性方法


# 下面写一个属性方法，这个属性方法写好之后的效果就是通过调用属性，来实现对方法的调用，类似于下面
# print(zhangsan.age)  # 这样调用属性就相当于调用方法print(zhangsan.get_age())


class Human():
    def __init__(self):
        self.__age = 0

    @property  # 修饰器        property平时用的还是比较多的
    def age(self):  # 相当于get_age方法
        return self.__age

    @age.setter
    def age(self, age):  # 相当于set_age方法
        if age > 0:
            self.__age = age
        else:
            print('年龄不合法')


p = Human()
p.age = 10  # 这样调用.age去赋值的话，就相当于执行.setter修饰器里头的set_age那个方法
print(p.age)  # 如果是这样不赋值，直接调用的话，相当于执行property修饰器里头的get_age方法


# 所以说白了，属性方法从字面理解，其实也是本质是做着方法的效果，但是调用的话，就用调用属性那样去调用


# 属性方法传入多个参数
class Dog():
    def __init__(self):
        self.__age = 0
        self.__name = '小狗'

    @property
    def messages(self):
        return self.__age, self.__name

    @messages.setter
    def messages(self, name):  # 默认就可以传入一个参数，如果多个参数就外加参数
        self.__age, self.__name = name


hashiqi = Dog()
hashiqi.messages = (10, '李四')
print(hashiqi.messages)
