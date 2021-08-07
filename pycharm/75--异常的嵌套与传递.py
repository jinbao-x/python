# 异常的嵌套
try:
    open('1.txt', 'r')
    for i in range(10):
        try:
            print(i / 0)
        except Exception as e:
            print(e)
except Exception as e:
    print('出错了，报错是{}'.format(e))


# 上面例子如果打开文件出错，则不会往下走，如果打开文件成功，后边的try进行错误捕获


# 异常的传递性
def test1():
    try:
        print(1 / 0)
    except Exception as error:
        print('出错了，报错是{}'.format(error))


def test2():
    test1()


def test3():
    test2()
