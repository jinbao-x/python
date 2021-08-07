# 面向对象是一种编程思想
'''
类：把具有相同属性和相同行为的东西归为一类，比如"人"、"车"，类是抽象的
对象：对象是类的具体实例
类-->对象-->(属性、行为)
'''


class Car():
    def run(self):
        print('车跑起来')

    def music(self):
        print('播放音乐')


taxi = Car()  # 创建一个面包车对象，初始化实例
taxi.run()  # 调用了run方法，车子跑起来


class Animal():
    def eat(self):  # 在方法定义里定义行为
        print('吃东西')

    def sleep(self):
        print('开始睡觉')


dog = Animal()  # 初始化实例，创建出来狗这个对象
dog.eat()  # 调用eat方法
dog.name = 'kitty'  # 给dog一个属性，名叫kitty，这种方法叫做给对象赋值属性
# 因为python可以动态赋值，所以这里可以这么用，但是不推荐，一般是在定义里边用构造方法定义属性
print(dog.name)
cat = Animal()
cat.sleep()  # 调用sleep方法
cat.name = 'mimi'  # 给cat一个属性，名叫mimi
print(cat.name)
