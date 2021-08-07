# 可以根据参数的不同的验证，而这个不同的验证可以写在同一个装饰器里(根据传入装饰器里的参数不同来决定)
def w(arg):  # 其实也就是在正常装饰器的基础上再套一层def，这样后面初始函数@修饰器的时候就不用@很多个不同的修饰器了，只需要写上参数即可
    # 而且，这样可以把多个类似的验证写在同一个修饰器里
    def new_get(fun):
        def inner(*args, **kwargs):
            if arg == 1:
                print('验证name')
            else:
                print('验证age')
            return fun(*args, **kwargs)

        return inner

    return new_get  # 注意这里面return返回的时候都不要加括号，因为是要返回函数地址的


@w(1)
def get_name(a, b):
    return a + b


@w(2)
def get_age(a, b):
    return a - b


print(get_name(5, 6))
print(get_age(6, 3))

# 增加日志、检查权限、取消CSRF、加上CSRF等等都可以用装饰器来做
