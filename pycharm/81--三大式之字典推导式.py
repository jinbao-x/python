ls = [0, 3, 34, 5, 56, 9, 20]
import random

i = random.choice(ls)  # choice方法是从中随机选值
d = {k: random.choice(ls) for k in range(5)}  # 也就是说字典前面还是写成键值对的形式，后面跟上结构
print(d)

# 代码整行上下调整快捷键是control+shift+上下键

# 字典推导式有时候可能会有这样的面试题
d1 = {"a": 1, "b": 2, "c": 3}
# 需要将上面这个字典里的key和value对调
d2 = {value: key for key, value in d1.items()}
print(d2)
