import random

while True:
    random_value = random.randint(1, 3)
    my_value = int(input('请输入你的值，1代表石头，2代表剪刀，3代表布'))
    if my_value == random_value:
        print('你和机器打成了平手')
    elif (random_value == 1 and my_value == 3) or (random_value == 2 and my_value == 1) or (
            random_value == 3 and my_value == 2):
        print('你赢了')
    else:
        print('你输了')
