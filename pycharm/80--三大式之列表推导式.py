# 列表推导式：生成列表
ls = []
for i in range(10):
    ls.append(i)
print(ls)

# 上面生成列表的方式还是有点复杂，下面使用列表推导式，简单地生成列表
ls1 = [i for i in range(10)]  # 这样把i写在最前面，然后后面跟上for结构，循环后的结果会自动添加到列表里
print(ls1)

# 如果要把10里的偶数这样的判断也放到列表推导式里呢？
ls2 = [i for i in range(10) if i % 2 == 0]  # 其实无非就是把几个简单的结构放到一个列表里，最前面写上结果

ls3 = [i for i in range(5) for j in range(4)]  # 也可以两个循环嵌套，等同于下面嵌套循环
ls4 = []
for i in range(5):
    for j in range(4):
        ls4.append(i)

ls5 = [(i, j) for i in range(5) for j in range(4)]  # 如果想返回两个，那就把这俩变量写成元组形式，等同于下面结构
ls6 = []
for i in range(5):
    for j in range(4):
        ls6.append((i, j))
print('ls5列表的结果为：{}'.format(ls5))
print('ls6列表的结果为：{}'.format(ls6))

# 那假如不想要列表里套元组的形式呢？想直接出来的ij结果就是按照前后排列直接存到列表里呢？
# 如果是普通的结构可以这么写
ls7 = []  # 新定义一个其他列表，然后再把刚ls6出来的列表套元组的形式转换一下，把元组里的元素拆开
for i in ls6:  # 用i遍历列表
    for j in i:  # 用j遍历元组
        ls7.append(j)  # 提取j并加入到新列表ls7里

# 以上这种其实也是比较好实现的，但是如果想要用列表推导式写该怎么写呢？其实也简单，通过上面普通结构的思路我们知道应该最终是取j的值
ls8 = [j for i in ls5 for j in i]  # 这样就完成了普通结构能完成的事
print(ls8)

# 还有其他相关用法
ls9 = [i ** 2 for i in range(10)]  # 将0到9的数的平方结果记录到列表里
print(ls9)

# 列表推导式是用来简化代码用到，不过如果一个复杂一点的结构强行写成列表推导式就会难读，所以一般用作简单结构的操作
