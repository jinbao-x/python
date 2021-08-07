# 函数其实也是一系列语句的结合
def print_name():  # 声明一个函数
    print('我叫老李')


print_name()


def show_name(name):  # 括号里的name代表参数
    print('我叫{}'.format(name))


show_name('张三')
