def test1():
    print('这是函数test1')
    test2()
    print('刚刚我在函数test1里调用了函数test2')


def test2():
    print('这是函数test2')


if __name__ == '__main__':
    test1()
