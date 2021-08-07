classes = []  # 先定义一个列表

# 列表的添加
classes.append('杨老师')
# 错误用法classes.append('王班长', '大个儿', '小个儿')
classes.append('王班长')
classes.append('大个儿')
classes.append('小个儿')
print(classes)  # 列表的打印

# 列表的删除
classes.remove('大个儿')  # 根据值删除，匹配即停止，只删除一次，如果列表里没有这个元素则会报错
print(classes)
classes.pop(2)  # 不写数字默认从末尾删除
print(classes)

# 列表的查找
name = classes[1]  # 列表是有序的，字典是而无序的
print(name)  # 打印列表里的元素

# 列表的修改，先找到某个元素然后再修改那个元素
classes[1] = '王组长'  # 班长犯错误降级到组长了，改名为王组长
print(classes)

# 列表插序，插入元素   来了个李校长，需要插到列表最前边
classes.insert(0, '李校长')
print(classes)

# 列表内插入列表
classes1 = ['赵同学', '钱同学', '孙同学', '李同学']
print(classes1)
classes.append(classes1)  # 这种属于班套班情况，也就是列表里包含列表，classes1列表为classes列表里的元素之一
print(classes)
classes.remove(classes[3])  # 把刚刚插入的classes1元素删除，以恢复原先的classes班级
print(classes)

# 合并列表(延展extend)
classes.extend(classes1)  # 这种属于列表延展
print(classes)
