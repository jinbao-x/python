class Dog():
    def __init__(self, name):  # 这种是实例属性
        self.name = name


hashiqi = Dog('哈士奇')
print(hashiqi.name)


# 现在想实现一个功能：想知道总共有多少个对象是这个类里的，也就是这个类有多少个实例

class Person():
    count = 0  # 这里是类属性，相当于函数版的全局变量，用于统计实例数量

    def __init__(self, name):  # 这种是实例属性
        self.name = name
        Person.count += 1


zhangsan = Person('zhangsan')
lisi = Person('lisi')
print('一共创建了{}个Person对象'.format(Person.count))

# 类属性在外部不一定非得要用Person.count才可以调用，用zhangsan.count也可以，也就是说类属性在外部，用对象也可以.它
# 不过类属性在内部的话，不能用self.count去操作它，因为self是操作实例，不是操作类
print('创建了{}个Person对象'.format(zhangsan.count))
