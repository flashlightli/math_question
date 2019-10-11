class A(object):

    def __setitem__(self, key, value):
        print("=======")

    # def __getitem__(self, item):
    #     print("111", item)
    #     return lambda **params: self.print(item, params) # return 一个匿名函数 参数作为dict传递

    # def __getattribute__(self, item):
    #     print("i am attrbute")

    def __getattr__(self, item):
        print("i am attr")
        return "2222"

    def print(self, method, params):
        print(method, params)


demo = A()
# print(dir(demo))
# print(demo['d'])
# print(demo['c'](user_id=2089278, a=2111))
print(demo.d)
#print(demo['w'])


# def print1(a):
#     print(a)
#
# f = lambda **x: print(x)
#
# f(user_id=193,uui=908)
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls)
        ob = ob.__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


def singleton(cls):
    instances = {}
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    pass

q = MyClass()


import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值，传对象的引用
c = copy.copy(a)  #对象拷贝，浅拷贝
d = copy.deepcopy(a)  #对象拷贝，深拷贝

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print('a = ', a, id(a))
print('b = ', b, id(b))
print('c = ', c, id(c))
print('d = ', d, id(d))

q = 3
w = 4
print(id(q), id(w))
