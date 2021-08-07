print("Hello Python")

'''
type()显示类型
str()转换为字符串类型
int()转换为整型类型
float()转换为float类型
bool()转换为布尔值
'''
num = 12
name = '鲁班'
gender = '男'
height = 1.62
desc = '矮个子'
b = True

print(num, name, gender, height, desc, b)  # 打印所有变量
print(float(num))  # 将int转换为float
print(int(height))  # 将float转换为int
print(str(num), str(height))  # 将int转换为str，将float转换为str
print(type(str(num)), type(str(height)))  # 使用type显示出类型
print(int(b))   # 将布尔值转为整型
print(bool(num))    # 将整数转为布尔值，非0即是真
