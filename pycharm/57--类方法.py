# 类方法，不能访问类属性，
class Dog():
    count = 0  # 定义一个类属性，辅助理解

    def __init__(self, name='小狗'):
        self.name = name

    @classmethod
    def get_name(cls):  # 类方法，可以访问类属性、也可以间接通过创建对象来访问类属性
        print(cls.count)  # 这里相当于在类方法里引用了类属性


hashiqi = Dog()
hashiqi.get_name()  # 这里使用hashiqi.表示get_name()这个类方法支持对象调用
Dog.get_name()  # 这里使用Dog.表示get_name()这个类方法支持类调用
