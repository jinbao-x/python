# str方法(__str__)的使用
class Chinese():
    def __init__(self, nationality='China'):
        self.nationality = nationality

    def __str__(self):
        return 'str方法的返回'

    def eat(self):
        print('吃东西')


zhangsan = Chinese('America')
print(zhangsan)  # str方法返回什么值，打印对象的时候就返回什么值
print(zhangsan.nationality)
