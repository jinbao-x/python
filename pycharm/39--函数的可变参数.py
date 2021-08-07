# 可变参数或不定长参数(*args,**kwargs)
def add(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(*args)  # 拆包
    print(args)  # 未拆包，返回元组
    print(kwargs)  # 字典


#   print(**kwargs)


add(1, 2, 3, 4, 5, 6, 7, 8)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, a=1, b=2)
