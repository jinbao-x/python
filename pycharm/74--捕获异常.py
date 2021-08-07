# 捕获一个错误
try:
    open('1.txt', 'r')
except FileNotFoundError:
    print('没有该文件')

# 捕获多个错误
try:
    open('1.txt', 'r')
    print('1 / 0')
except (FileNotFoundError, ZeroDivisionError):
    print('报错...')

# 捕获所有异常
try:
    open('1.txt', 'r')
except Exception:
    print('有错误')

# 捕获具体错误信息
try:
    open('1.txt', 'r')
except Exception as result:
    print('有错误，错误信息是{}'.format(result))
else:
    print('没有异常')
finally:
    print('hahaha')  # 不管有没有异常都会执行，可以做一些想要的必须操作
