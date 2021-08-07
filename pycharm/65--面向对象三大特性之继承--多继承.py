# class A(object):  # 在python3中这个object不写其实也可以
#     def a(self):
#         print('这是a方法')
#
#
# class B(object):
#     def b(self):
#         print('这是b方法')
#
#
# class C(object):
#     def c(self):
#         print('这是c方法')
#
#
# class D(A, B, C)
#     def d(self):
#         print('这是d方法')
#
#
# dada = D()
# dada.a()  # 继承了三个爸爸的方法，这就叫多继承
# dada.b()
# dada.c()
# dada.d()


# 注意：
class A(object):  # 在python3中这个object不写其实也可以
    def a(self):
        print('这是A类的a方法')


class B(A):
    def a(self):
        print('这是B类的a方法')


class C(A):
    def a(self):
        print('这是C类的a方法')


class D(B, C):
    def d(self):
        print('这是d方法')


class F(D):
    def f(self):
        print('这是f方法')


# 根据上面类的定义，可以看到类的继承过程是
# A(a) --> {B(a)C(a)} --> D --> F

fangfang = F()
fangfang.a()  # 注意这里最终调用的a方法到底是谁的

# 最终的结果是B类的a方法，这是因为B和C重写了父类的a方法，所以其下的子类不会找到A类的a，而B和C都是D的父亲，那么由于B在C前面定义，因此D类先认B作为自己的亲爸爸
