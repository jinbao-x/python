# 返回值和在函数内直接print有很大区别
# print只是把变量打印到了控制台上，而且也只有这一个作用
# 返回值可以另外加以利用，可以存到变量里，然后想怎么使用变量随意

def add(x, y):
    z = x + y
    print(z)  # 注意这个函数是没有返回值的


if __name__ == '__main__':
    result = add(1, 2)  # 因为函数没有返回值，所以result存了个寂寞
    print(result)


def show(x, y):
    z = x + y
    return z  # 这里将z作为返回值返回，且函数体内return后边的代码不会继续执行


if __name__ == '__main__':
    result = show(2, 4)  # 利用了函数的返回值
    print(result)


# 有了返回值这个"功能",调用函数就不需要考虑函数内部是如何实现的，只需要知道用什么样的参数可以得到什么样的结果

# 返回多个值
def process(name, age):
    name = '我的名字是{}'.format(name)
    age = '我的年龄是{}岁'.format(age)
    return name, age  # 如果是放回多个参数，那么返回值会以元组的形式存在，因此对返回值处理的时候需要对元组进行处理


if __name__ == '__main__':
    result = process('老王', 23)
    print(result[0], result[1])
