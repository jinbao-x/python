'''
士兵突击
    枪类
        装子弹
        开火
    士兵
        开枪
'''


class Gun():
    def __init__(self, kind='步枪'):
        self.kind = kind

    def loading(self):
        print('正在给枪膛装子弹')

    def fire(self):
        print('开火')


class Officer():
    def __init__(self, rank='士兵'):
        self.rank = rank

    def shooting(self, gun):
        print('我是一个{}，我发现了间谍，我现在开枪弄死他'.format(self.rank))
        gun.loading()
        gun.fire()


class Person():
    def __init__(self, standard='好人'):  # 默认这个人是好人
        self.standard = '好人'

    def steal(self):
        print('我是一个间谍，我要完成任务，所以我现在要拿起匕首准备拆保险箱')  # 做拿刀的动作
        self.standard = '坏人'  # 既然要拿偷东西，那么就把他的标志属性赋值成坏人


zuolun = Gun('左轮')  # 出场第一个对象：枪类左轮
lianzhang = Officer('连长')  # 出场第二个对象，官兵
# 事现定义好群众演员，以及唯一一个潜伏已久的间谍
zhangsan = Person()
lisi = Person()
wangwu = Person()
# 这些Person不知道谁是好人谁是坏人，如果偷文件了，就会触发standard为坏人
# 也就是说，如果是好人，你就不要作死做steal动作偷文件，一旦你偷，我就判定你是间谍

safe_box = 0  # 定义一个保险箱，默认为0则表示保险箱里还没放东西，大于等于1表示已经有机密文件

# 出现一个人，通过判断那个人手里有没有匕首，判断其是否是敌人，如果是则zhangsan完成开枪射击的动作
if __name__ == '__main__':
    mark = True
    while mark:  # 24h不间断巡逻
        safe_box = int(input('请确认是否往保险箱里放东西：'))
        if safe_box != 0:  # 如果非0则表示有了机密文件，触发间谍去做盗窃任务
            lisi.steal()  # 注意这里！注意这里！不是间谍的人是不会做这个steal动作(偷机密文件)的，这个女孩做steal了那么她完了！
            if zhangsan.standard == '坏人':
                print('找到了潜伏已久的间谍，这个间谍名字是zhangsan')
                lianzhang.shooting(zuolun)  # 传入zuolon这个对象当作shooting方法的参数
                mark = False  # 既然杀死了间谍，安保可以取消了
            if lisi.standard == '坏人':
                print('找到了潜伏已久的间谍，这个间谍名字是lisi')
                lianzhang.shooting(zuolun)  # 传入zuolon这个对象当作shooting方法的参数
                mark = False  # 既然杀死了间谍，安保可以取消了
            if wangwu.standard == '坏人':
                print('找到了潜伏已久的间谍，这个间谍名字是wangwu')
                lianzhang.shooting(zuolun)  # 传入zuolon这个对象当作shooting方法的参数
                mark = False  # 既然杀死了间谍，安保可以取消了

# 注意看上面的main函数里的if判断，军官为了判断哪一个对象是间谍，则对这些对象一一甄别，可是这意味着要写好多个判断，如何直接获取某个类里的所有对象呢？
# 需要用到后面的知识点了，等到后边再对此案例修改
