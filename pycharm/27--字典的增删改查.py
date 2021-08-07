# 字典的增删改查
d = {}
d['id'] = 1
d['name'] = 'tom'
d['性别'] = '男'
d['性别'] = '女'  # 用这种方式添加键值对，如果键已经存在，则会进行更新
d['爱好'] = '看书'
print(d)

# 字典的添加
d['手机'] = 13456778988
d.setdefault('婚姻状况', '已婚')  # 用这个也能添加，不过和上边区别在于，这个不会更新已经存在的键，如果键已经存在，则不作处理
d.setdefault('婚姻状况', '未婚')
print(d)

# 字典的删除操作，根据键删除
d.pop('爱好')
print(d)
# d.popitem()   # 这种方式删除是从字典里随机删除一个

# 字典的查询
name = d['name']  # 用d['name']的方式查找，找到后赋值给name
print(name)
name = d.get('name')  # 建议用这种get的方式查找，如果没找到这个键，不会返回报错，会返回None
print(name)
key = d.keys()  # 获取所有的键
print(key)
value = d.values()  # 获取所有的值
print(value)
item = d.items()  # 获取所有的键值对
print(item)

# 字典的合并
d1 = {'id': 1, 'name': 'tom', '性别': '男', '手机': 13456778988}
d2 = {'爱好': '女', '住址': '上海'}
d1.update(d2)
print(d1)
