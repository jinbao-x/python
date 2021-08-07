# class Dog():
#     def eat(self):
#         print('吃饭')
#
#     def guard(self):
#         print('看家')
#
#
# class Cat():
#     def eat(self):
#         print('吃饭')
#
#     def catch(self):
#         print('捉老鼠')
#
#
# hashiqi = Dog()
# mimi = Cat()
# 在上面这两个类的定义中，可以看到两个类其实有一个类似的方法，那么这个方法可以写在父类

# python中顶级父类是object
class Animals():  # 在python3中这个object也可以不写
    def __init__(self):
        self.gender = '雄性'

    def eat(self):
        print('吃饭')


class Dog(Animals):  # 继承Animal父类
    def guard(self):
        print('看家')


class Cat(Animals):
    def catch(self):
        print('捉老鼠')


hashiqi = Dog()
mimi = Cat()
hashiqi.eat()  # 会继承Dog类的父类，也就是Animals对象的方法
mimi.eat()  # 会继承Cat类的父类，也就是Animals对象的方法
print(hashiqi.gender)  # 会继承Dog类的父类，也就是Animals对象的属性

# 继承
# 1、如果不同类中有相同的行为，可以用继承，这样可以减少代码，实现代码复用
# 2、子类可以从父类把属性和方法都继承过来
# 3、继承具有传递性，不管有多少层继承，都会往上继承
