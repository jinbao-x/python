# 一些常用快捷键：
# 使用ctrl+alt+L可以统一一下代码格式
# 使用ctrl+/可以快速注释多行

age = int(input('请输入年龄'))
if age >= 80:
    print('祝您长命百岁')

name = input('请输入名字')
if name == '程咬金':
    print('这个英雄好肉')

if age >= 80:
    print('祝你长命百岁')
elif (age < 80) and (age >= 20):  # and且 or或 not取反
    print('祝您事业有成')
else:
    print('祝您成绩优异')

num1 = float(input('请输入第一个数字'))
num2 = float(input('请输入第二个数字'))
ysf = input('请输入运算符(+-*/)')
if ysf == '+':
    print('%f+%f=%.2f' % (num1, num2, num1 + num2))
    print('{}+{}={:.2f}'.format(num1, num2, num1 + num2))
elif ysf == '-':
    print('%f-%f=%.2f' % (num1, num2, num1 - num2))
    print('{}-{}={:.2f}'.format(num1, num2, num1 - num2))
elif ysf == '*':
    print('%f*%f=%.2f' % (num1, num2, num1 * num2))
    print('{}*{}={:.2f}'.format(num1, num2, num1 * num2))
elif ysf == '/':
    print('%f/%f=%.2f' % (num1, num2, num1 / num2))
    print('{}/{}={:.2f}'.format(num1, num2, num1 / num2))