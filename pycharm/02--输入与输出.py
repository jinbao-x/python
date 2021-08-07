name = 'xujinbao'
age = 23
height = 1.70
'''
%s 格式化为字符串
%d 格式化为整数
%f 格式化为浮点数
使用format进行格式化输出
{}占位符并进行格式化设置   .format()置入变量并格式化输出
'''
print('我的名字是', name)
print('我的身高是%s米' % height)
print('我的身高是%f米' % height)

print('我的名字是%s我的年龄是%d我的身高是%0.2f米' % (name, age, height))  # 格式化输出
print('我的名字是{}我的年龄是{}我的身高是{:.2f}'.format(name, age, height))
print('我的名字是{0}我的年龄是{1}我的身高是{2:.2f}'.format(name, age, height))

# weight = input('请输入重量')
# price = input('请输入价格')
# print('总价格是%f' % (weight * price))     # 注意用这个会报错，因为input输入的都是字符串
# 所以需要把输入进去值转为想要的类型

weight = float(input('请输入重量'))
price = float(input('请输入价格'))
print('总价格是%0.2f元' % (weight * price))

num = int(input('请输入百分比的数值'))
print('%d%%' % num)  # 想打印出%这个字符的话，需要使用两个百分号%%
print('{}%'.format(num))    # 或者采用这种占位符的方式
