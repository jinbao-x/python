def new_get_name(fun):
    def inner(a, b):
        return fun(a, b)  # 一般情况下要加return避免返回None
        pass

    return inner


@new_get_name
def get_name(a, b):
    return a + b


print(get_name(1, 2))

# 上面new_get_name()函数里那样写虽然也行，但是真实的get_name()的参数太多的话，上面也对应写那么多参数容易疯掉，建议用**args **kwargs
# 示例如下
# def new_get_name(fun):
#     def inner(*args, **kwargs):
#         print('验证')
#         return fun(*args, **kwargs)
#
#     return inner
#
#
# @new_get_name
# def get_name(a, b):
#     return a + b
#
#
# print(get_name(1, 2))
