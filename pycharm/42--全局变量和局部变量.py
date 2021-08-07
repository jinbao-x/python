name = '张三'
age = 23


def show():
    # global name, age  # 声明name, age为全局变量
    name = '李四'
    age = 100
    print('我在函数内部，我目前的名字是：{}，目前的年龄是{}'.format(name, age))


if __name__ == '__main__':
    show()
    print('我现在是在main里，我最终的名字是：{}，我最终判定的年龄是{}'.format(name, age))
