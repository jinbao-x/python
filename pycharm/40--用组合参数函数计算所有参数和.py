def add(x, y, z=3, *args, **kwargs):
    isum = 0
    isum = x + y + z
    for i in args:
        isum += i
    for j in kwargs.values():  # .values是获取字典的所有值
        isum += j
    print(isum)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, a=1, b=45, c=89)
