# 静态方法：尽量不引用类属性、实例属性、实例方法，它是一个独立的个体
import time


class Dog():
    desc = '哈哈'

    def __init__(self):
        self.name = '老王'

    @staticmethod  # 使用静态方法
    def get_time(args="当前时间"):  # 括号里不能写self，但是可以写参数，也就是说这里边不要引用类属性、实例属性，尽量保证是独立的，否则违背静态方法的本质
        return args + time.strftime('%Y-%m-%d')


hashiqi = Dog()

print(hashiqi.get_time())  # 静态方法支持对象(hashiqi)调用
print(Dog.get_time())
print(Dog.get_time("当前时间是"))  # 静态方法支持类(Dog)调用
