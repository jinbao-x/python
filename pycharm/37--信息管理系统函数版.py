# 添加信息
def add_messages():
    d = {}
    name = input('请输入名字：')
    age = int(input('请输入年龄：'))
    gender = input('请输入性别：')
    d['name'] = name
    d['age'] = age
    d['gender'] = gender
    ls.append(d)
    print("信息添加成功！")


# 查找信息(根据name)
def find_messages():
    name = input('请输入要查找的人名：')
    flag = False
    for i in ls:
        if i.get('name') == name:
            print('已为您查询出来如下信息：')
            print('姓名：{}\n年龄：{}\n性别：{}\n'.format(i['name'], i['age'], i['gender']))
            flag = True
            break
    if not flag:  # 如果没有这个人那么flag按道理是False，那么not flag就是真
        print('找不到这个人！')


# 更改信息(根据name)
def change_messages():
    name = input('请输入要修改的人名：')
    flag = False
    for i in ls:
        if i.get('name') == name:
            which = input('请输入你想修改的信息(name/age/gender)：')
            change = input('请输入要改的内容：')
            i[which] = change
            print('已经修改成功！更新后的内容如下：')
            print('姓名：{}\n年龄：{}\n性别：{}\n'.format(i['name'], i['age'], i['gender']))
            flag = True
            break
    if not flag:  # 如果没有这个人那么flag按道理是False，那么not flag就是真
        print('找不到这个人！')


# 删除信息(根据name)
def delete_messages():
    name = input('请输入要删除的人名：')
    flag = False
    for i in ls:
        if i.get('name') == name:
            ls.remove(i)
            print('已经成功删除！')
            flag = True
            break
    if not flag:  # 如果没有这个人那么flag按道理是False，那么not flag就是真
        print('找不到这个人！')


print('欢迎使用信息管理系统！')
ls = []
while True:
    print('目前信息管理系统里的信息如下：\n{}'.format(ls))
    print('1、增加个人信息')
    print('2、查找个人信息')
    print('3、修改个人信息')
    print('4、删除个人信息')
    print('5、退出')
    choice = input('请输入功能编号(1/2/3/4/5)：')
    if choice == '1':
        add_messages()
    elif choice == '2':
        find_messages()
    elif choice == '3':
        change_messages()
    elif choice == '4':
        delete_messages()
    elif choice == '5':
        print('退出管理系统！')
        break
    else:
        print('输入编号有误！请检查后重新输入功能编号：')
