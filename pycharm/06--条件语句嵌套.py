gender = input('请输入性别')
if gender == '男':
    print('不感兴趣')
elif gender == '女':
    attractivenes = input('请输入颜值吸引力(beauty,ugly)')
    if attractivenes == 'beauty':
        print('可以交个朋友')
    elif attractivenes == 'ugly':
        print('不感兴趣')
    else:
        print('考虑考虑')
else:
    print('不考虑')
