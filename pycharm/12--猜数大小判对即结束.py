import random
# 像这种死循环，如果想打破循环，那就破坏判断条件
# 如果不是死循环，而是一定范围内的循环，可以专门判断一下某个条件，若满足则使用break终止同一层级的整循环
# 而continue则是跳过当次循环，当次循环内continue后边的内容不执行，但是循环还会继续

random_value = random.randint(1, 100)
mark = True
count = 0
while mark:
    my_value = int(input('请输入你的数值(1-100)'))
    if my_value == random_value:
        print('恭喜你猜对了')
        mark = False
    elif my_value >= random_value:
        print('你猜大了')
    else:
        print('你猜小了')
    count += 1
print('你总共猜了{}次'.format(count))
