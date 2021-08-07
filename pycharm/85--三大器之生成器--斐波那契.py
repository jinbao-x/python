# 1 1 2 3 5 8 13 21......
# 也就是后面的数是前面两个数的和

def fib(num):
    i, a, b = 0, 0, 1  # i用来控制循环
    while i < num:
        yield b  # 先生成1
        a, b = b, a + b
        i += 1


g = fib(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 这里利用生成器实现了边生成边返回
