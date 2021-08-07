Sum1 = 0
for i in range(1, 101):
    if i % 2 != 0:
        Sum1 += i
print(Sum1)

# 或者
Sum2 = 0
for i in range(1, 101, 2):
    Sum2 += i
print(Sum2)
