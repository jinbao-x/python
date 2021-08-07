# 递归函数是函数自己调用自己，因此这要求递归函数必须要有终止条件，否则将陷入死循环
# 阶乘
# 6！= 6*5*4*3*2*1

def jiecheng(num):
    if num == 1:
        return num
    isum = num * jiecheng(num - 1)
    return isum


result = jiecheng(6)
print(result)
