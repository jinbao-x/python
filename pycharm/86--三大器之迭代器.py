# 可迭代对象：能用for循环遍历的那些数据都是可迭代对象
# list、dict、tuple(元组)、str

from collections.abc import Iterable  # Iterable是可迭代对象,collection加.abc就可以不报DeprecationWarning警告，了解即可

print(isinstance([], Iterable))  # isinstance判断某个东西是不是某个类的实例
# 上面这个是判断[]列表是不是可迭代对象的实例，Iterable是可迭代对象的意思，Iterator是迭代器
print(isinstance(str, Iterable))
# 迭代器：能用next()方法的叫迭代器
# ls = [1, 3, 5]
# next(l)   # 可以发现列表是不可以用next()方法的，其实前边讲过的生成器可以用next()方法

g = (i for i in range(10))
print(next(g))  # 可以发现生成器就可以用next()方法，所以生成器其实也是一种特殊的迭代器，也是可迭代对象

# 可以把可迭代的对象转成迭代器(能用next()方法)
ls1 = [1, 2, 3, 4]
ls2 = iter(ls1)
print(next(ls2))
print(next(ls2))
print(next(ls2))
print(next(ls2))

# 迭代器优点：
# 1、迭代器惰性计算，节省内存
# 2、迭代器不依赖索引，可以没有索引的对象，字典，集合
# 迭代器缺点
# 1、无法获取迭代器长度
# 2、只能往后取值，不能倒着取值
