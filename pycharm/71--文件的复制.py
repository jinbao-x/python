f1 = open('00--test.py', 'r')
content = f1.read()
f1.close()

f2 = open('00--test1.py', 'w')
f2.write(content)
f2.close()
