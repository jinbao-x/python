def check_login1(fun):
    def check():
        print('开始验证1：已经登录了账户')
        fun()

    return check  # 注意不能有括号，因为是要返回地址


def check_login2(fun):
    def check():
        print('开始验证2：已经获取到账户信息')
        fun()

    return check  # 注意不能有括号，因为是要返回地址


def check_login3(fun):
    def check():
        print('开始验证3：余额够')
        fun()

    return check  # 注意不能有括号，因为是要返回地址


@check_login1
@check_login2
@check_login3
def get_name():
    print('可以买东西了')


get_name()
