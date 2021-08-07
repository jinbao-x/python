# 对象的初始化方法--定义对象的属性
class Chinese():
    def __init__(self):  # 构造方法、魔法方法、初始化方法      init方法后边不需要调用，会在创建对象的时候直接初始化
        print('init')
        self.nationality = 'China'  # 为对象本身创建初始化属性
        self.complexion = 'yellow'

    def eat(self):
        print('吃东西')

    def sleep(self):
        print('睡觉')


xiaoming = Chinese()  # 通过结果可以看到
print('1')
xiaoming.eat()
print('2')
xiaoming.sleep()
print('3')
print(xiaoming.nationality)


# 初始化方法(__init__)的多个参数的使用
class Chinese():
    def __init__(self, nationality='China', complexion='yellow'):  # 这里的参数除了对象本身，额外定义了两个参数
        self.nationality = nationality  # 该属性从参数接收
        self.complexion = complexion

    def eat(self):
        print('吃东西')


laowang = Chinese('America')  # 第二个参数没有传，则使用的默认参数，并且由于给的参数没有用nationality=America指定，则默认这个America就是传给第一个参数
print(laowang.nationality)
print(laowang.complexion)
