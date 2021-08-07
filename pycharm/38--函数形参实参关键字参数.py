def calculate(a, process='+', b=4):  # 这里的a,b,process是形参，同时因为b=4直接定义了默认值，这意味着调用该函数时不必传此参数
    if process == '+':
        num = a + b
    elif process == '-':
        num = a - b
    elif process == '*':
        num = a * b
    elif process == '/':
        num = a / b
    else:
        print('您输入了不支持的计算符号')
    print('最终计算结果为：{}'.format(num))


first = float(input('请输入第一个数：'))
second = float(input('请输入第二个数：'))
process = input('请输入想进行的计算：')
calculate(first, process, second)  # 这里的a,b,process是实参。因为函数里定义的是形参，函数声名处的参数只在函数体内部使用

# 此处a=,b=的参数形式叫做关键字参数，最主要的用法是这么定义可以改变参数的前后位置，而不必按照函数声明里的参数的位置书写
calculate(b=3, a=324, process='+')

# 不传入b参数
calculate(3, '*')
calculate(3)
