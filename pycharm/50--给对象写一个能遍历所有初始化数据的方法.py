class A():

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def list_all_members(self):
        for i, j in vars(self).items():
            print(i, j)


aaa = A()
aaa.list_all_members()
