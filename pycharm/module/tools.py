def add(x, y):
    return x + y


def jian(x, y):
    return x - y


class Tool(object):
    def multi(self, x, y):
        return x * y

    @classmethod
    def show(cls):
        print('调用了类方法')
