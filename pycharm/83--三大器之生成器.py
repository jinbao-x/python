# 一边循环一边计算来生成想要的数字类
# ls = [0, 2, 4, 6, 8, 10.....]
# 按照规律，用到多少就生成多少
ls1 = [i for i in range(100) if i % 2 == 0]
print(ls1)

g = (i for i in range(100) if i % 2 == 0)
print(g)  # 可以看到生成的是一个对象
print(next(g))
print(next(g))

ls2 = []
for i in range(3):  # 生成三个
    ls2.append(next(g))
print(ls2)

# 把列表推导式换成小括号，用next(g)
# 或者用g.__next__()

# 生成器实际上保存的是一种算法
