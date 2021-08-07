class Dog():
    count = 1  # 这里定义一个类属性，用于辅助理解"后边类方法可以引用类属性"

    # 初始化方法、构造方法、初始化方法
    def __init__(self):  # 不需要主动调用
        self.name = 'zhangsan'  # 这里定义一个对象属性，用于辅助理解后边的"类方法通过创建对象来调用对象属性"

    # 实例方法
    def show(self):  # 支持对象调用，不支持类调用，因为这是实例(self)的方法
        print('haha')

    # 静态方法
    @staticmethod
    def get_desc():  # 不能引用类属性和实例属性，其本身单独使用，也即意味着括号里不要手贱写self
        print('描述信息')

    # 类方法
    @classmethod
    def get_name(cls):  # 可以访问类属性，也可以间接的通过创建对象来访问对象属性
        print(cls.count)

    @classmethod
    def create_obj(cls):
        return cls().name  # 这里使用cls()表示创建对象，然后.name调用这个对象的name属性，这意味着通过创建对象来访问对象属性


hashiqi = Dog()

hashiqi.show()  # 这里用的hashiqi.调用的实例方法show()，表明实例方法支持对象调用
# Dog.show()  # 这里用类Dog.调用实例方法show()会报错，表示实例方法不支持类调用

hashiqi.get_desc()  # 这里用的hashiqi.调用的静态方法get_desc()，表明静态方法支持对象调用
Dog.get_desc()  # 这里用的Dog.调用的静态方法get_desc()，表明静态方法支持类调用

hashiqi.get_name()  # 这里用的hashiqi.调用的类方法get_name()，表明类方法支持对象调用
Dog.get_name()  # 这里用的Dog.调用的类方法get_name()，表明类方法支持类调用

print(Dog.create_obj())  # 直接调用类方法，而这个类方法里通过创建对象cls()来访问对象属性.name
