import subprocess

output = subprocess.check_output(['df', '-h'])
output = output.decode("utf-8")  # 因为本身获取过来的就是ASCII，而utf-8本身又是兼容ASCII的，所以即便是开头写了# encoding: utf-8也还是显示有问题
# 因此这里强制转换一下字符串

print(output)
lines = output.split('\n')
print(lines)
