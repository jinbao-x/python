# 面向对象的三大特性：封装、继承、多态
class Dog():
    def __init__(self, age, name='小狗'):
        self.name = name
        self.age = age

    def wangwang(self):
        print('汪汪叫')

    def sleep(self):
        print('睡觉')


dog = Dog(23)
print(dog.name)  # 这其实已经体现了封装，调用封装好的属性
dog.sleep()

# 封装
# 1、把属性封装到对象当中
# 2、上述示例中封装了多种方法，封装到一个对象中，方便调用
# 3、
