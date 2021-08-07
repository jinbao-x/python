class Software_test():
    def buy(self):
        return '购买成功'

    def check_money(self, money):  # 看一下钱够不够
        if money < 100:  # 钱小于100买不了
            print('钱不够')
        else:
            return self.buy()  # 不加return仅仅只是调用，会导致在print这个check_money这个方法的时候会打印出来None，因此需要将这个调用方法返回


tianmao = Software_test()
print(tianmao.check_money(200))

print(tianmao.buy())  # 注意看这里，不判断钱够不够直接调用该方法竟然也成功了...这样不行的，算是一种bug，因此下面定义一个私有方法


class Software():
    def __buy(self):  # 定义私有方法，只有函数体内可以调用它
        return '购买成功'

    def check_money(self, money):  # 看一下钱够不够
        if money < 100:  # 钱小于100买不了
            print('钱不够')
        else:
            return self.__buy()  # 这里调用私有方法


jingdong = Software()
print(jingdong.check_money(300))

# 私有方法可以避免直接被调用，也影响子类调用
