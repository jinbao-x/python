# 异常中抛出异常什么意思呢？捕获到了异常，但又抛出去了，谁爱处理谁处理
try:
    open('1.txt', 'r')
except Exception as e:
    raise
