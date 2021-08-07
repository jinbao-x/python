ls = [12, 34, 22, 143, 12, 34]
ls_new = []
for i in ls:
    if i not in ls_new:
        ls_new.append(i)
print(ls_new)

# 打印出嵌套列表里的所有元素
ls = [[12, 23, 45], [453, 21, 12]]
for i in ls:
    for j in i:
        print(j)
