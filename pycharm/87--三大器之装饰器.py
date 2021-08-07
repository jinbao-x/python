# 开放：对外扩展是开放的
# 封闭：对于修改是封闭的

def check_login(fun):  # 这里的fun是个形参，没有实际意义
    def check():
        print('做验证')  # 这是新的函数要执行的操作，可以做验证登录等的验证东西，如果验证成功，就可以执行fun()，其实也就是真实的get_name()那部分操作
        fun()  # 这里使用形参加括号，相当于又执行了初函数get_name()

    return check  # 返回函数地址


def get_name():
    print(name)


get_name = check_login(get_name)  # 注意这里把get_name传进去了，get_name没有括号，意味着传入的是get_name地址
# 但是由于check_login返回的是check函数的地址，这意味着该get_name = check_login(get_name)赋值赋完之后，再用get_name指向的函数地址变了
get_name()

# a = get_name  # 不加括号就是函数的地址
# a()  # 这样其实也相当与调用get_name函数


# 不过上面那个get_name = check_login(get_name)以及get_name()这样的调用写法虽然确实实现了不修改初始函数里边本有的结构
# 而是另外加函数进行验证判断等等，可是代码写的太复杂，也不是修饰器的真正写法，真正的修饰器写法是在初始函数头上加个@check_login
# 示例如下
# def check_login(fun):
#     def check():
#         print('做验证')
#         fun()
#
#     return check
#
#
# @check_login
# def get_name():
#     print(name)

# 修饰器说白了就是使用@check_login这样的引用当做帽子扣在某个函数上，
# 样那个函数就不用修改里边的东西加判断之类的了，要做验证的话，只需要该修饰器里的内容加判断即可

# 闭包：当函数内部还有一个函数，并且这个函数用到了外部函数的变量，这个函数和变量统称为闭包
