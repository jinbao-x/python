class House():
    def __init__(self, color='红色', size='大'):
        self.color = color
        self.size = size

    def __str__(self):
        return '可是真不错呢，一个房子被创建出来了'

    def opendoors(self):
        print('房子是{}的，房子为{}房子，现在已一键打开所有门欢迎新主人入住'.format(self.color, self.size))


hotel = House(size='小')
print(hotel)

# 这样的用法是错的，hotel.opendoors是对象的方法，不是对象的属性，不要用print,否则会先执行opendoors行为然后再print出来个None，这显然不是想要的
# print(hotel.opendoors())

hotel.opendoors()

print(hotel.size)
