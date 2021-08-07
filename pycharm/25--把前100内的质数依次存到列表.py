ls = []
for i in range(2, 101):
    flag = True  # 加个标志变量，先假设是质数
    for j in range(3, i):
        if i % j == 0:
            flag = False  # 如果有任意一种除法不满足质数，则推翻假设
            break
    if flag:
        ls.append(i)
print(ls)
