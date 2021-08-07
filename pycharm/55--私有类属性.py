# 私有类属性的获取
class Person():
    __count = 0  # 这里是类属性，相当于函数版的全局变量，用于统计实例数量

    def __init__(self, name):  # 这种是实例属性
        self.name = name
        Person.__count += 1

    # 注意下面的用法，get_count()括号里不要传self，self相当于对象本身
    def get_count():  # 定义一个公有方法，返回私有类属性
        return Person.__count  # 返回类的私有属性


zhangsan = Person('zhangsan')
lisi = Person('lisi')
wangwu = Person('wangwu')
print(Person.get_count())

# 总结一下：
# 私有不私有是相对于外部来说的，也就是想不想让外部访问
# 而类属性或者是实例属性的区别在于作用域，是针对类还是针对实例
