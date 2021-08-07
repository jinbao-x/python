# 使用sort直接修改列表里元素的顺序
ls = [5, 8, 1, 10, 13]
ls.sort()  # sort默认为升序  sort()是列表里专有的方法，而sorted对于所有可迭代序列均可以使用
print(ls)
ls.sort(reverse=True)  # 设置为降序
print(ls)

# 想修改元素顺序，并返回新的列表，则使用sorted
ls = [13, 78, 34, 12, 90, 1]
ls_new = sorted(ls, reverse=True)
print(ls)
print(ls_new)

# 反转列表里的元素
ls = [23, 56, 7, 8, 23, 90, 45]
ls.reverse()
print(ls)
