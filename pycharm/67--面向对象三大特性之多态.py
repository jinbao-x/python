# 多态
# 多态的前提是继承和重写

class Organism(object):
    def play(self):
        print('玩')


class MarineOrganism(Organism):  # 海洋生物
    def play(self):
        print('水里游来游去')


class TerrestrialOrganism(Organism):  # 陆地生物
    def play(self):
        print('地上跑来跑去')


class Turtle(Organism):
    def action(self, status):
        status.play()  # 海龟的action方法传入一个参数，而这个参数可以用来传入对象，以此实现，不同对象调用相同的方法，得到不同的状态


large_turtl = MarineOrganism()
medium_turtl = TerrestrialOrganism()
small_turtl = Turtle()

small_turtl.action(large_turtl)
small_turtl.action(medium_turtl)  # 传入的参数是陆地生物这个类的实例对象，那么其.play()方法将是对应的方法
small_turtl.action(small_turtl)  # 这个传入的参数是自身，那么自己的.play()方法将从父类Organism里继承

# 调用了同一种行为，产生了不同的结果，这就叫做多态
