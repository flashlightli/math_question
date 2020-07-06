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

# 闭包
def my_func(*args):
    fs = []
    for i in range(3):
        def func():
            return i * i
        fs.append(func)
    return fs


fs1, fs2, fs3 = my_func()
print(fs1())
print(fs2())
print(fs3())


# 解决一个问题
# 构造方法中的初始值无法继承的问题
class A(object):
    def __init__(self):
        self.nameaa = 'aa'

    def funca(self):
        print('function a %s' % self.nameaa)


class B(A):
    def __init__(self):
        self.namebb = 'bb'
        # 它会查找所有的超类，以及超类的超类，直到找到所需的特性为止。
        super(B, self).__init__()

    def funcb(self):
        print('function b %s' % self.namebb)


b = B()
print(b.namebb)
b.funcb()
print(b.nameaa)
b.funca()


# 使用 super() 可以很好地避免构造函数被调用两次。
class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


d = D()

"""
输出结果
enter D
enter B
enter C
enter A
leave A
leave C
leave B
leave D
"""


demo = [1, 2, 3, 4]
it_demo = iter(demo)
for i in it_demo:
    print(i)

def decor_arg(acc):
    def decor(func):
        def wrapper(*args, **kwargs):
            print("222", acc)
            result = func(*args, **kwargs)
            return result

        return wrapper
    return decor

@decor_arg(acc = 1)
def demo_print():
    print("111")

# demo_print()
print("======")


def test_print(value):
    print("111111")
    return value


def gen():
    value = 0
    while True:
        receive = yield test_print(value)
        if receive == 'e':
            break
        value = 'got: %s' % receive

g=gen()
print(next(g))     # g.send(None)
print(g.send('hello'))
print(g.send(123456))
# print(g.send('e'))

print("=======")


def g1():
    yield range(5)


def g2():
    yield from range(5)


it1 = g1()
it2 = g2()
print(it1)
for x in it1:
    print(x)

for x in it2:
    print(x)


print("==-==")
def test_pr(x):
    print("====", x)
    return x + 1


def gen_test1():
    print("before 222")
    yield test_pr(2)
    print("222")

    yield test_pr(3)


def gen_test2():
    print("before 222")
    yield test_print(3)
    print("222")


q1 = gen_test1()
# q2 = gen_test2()
# import pdb
# pdb.set_trace()
print(next(q1), next(q1))


print("111111====11111")
def test_gen_1():
    while True:
        print("1")
        yield 2
        print("3")


qq = test_gen_1()
print(next(qq))
print(next(qq))

print("12======")
def generator2():
    num = yield 1
    print("--1--", num)
    yield 2
    yield 3
    return 4

gen = generator2()
print(gen.send(None))  # 如果使用send()的时候，第一个传入的值必须是None，因为当调用send()的时候，才执行到第一个yield，只能输出一个值，不能接收值。
print(gen.send(101))
print(gen.send(None))
gen.close()


def retry(times=1):
    def decor(func):
        def wrapper(*args, **kwargs):
            curr_time = 0
            result = None
            while curr_time < times:
                try:
                    result = func(*args, **kwargs)
                except:
                    curr_time += 1
                else:
                    break

            return result
        return wrapper
    return decor


class TreeNode(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def get_right_list(root):
    result = []
    if not root:
        return []

    tmp_node = [root]
    while tmp_node:
        node_value = None
        tmp_node_list = []
        for node in tmp_node:
            tmp_node_list.append(node.left)
            tmp_node_list.append(node.right)
            node_value = node.value
        tmp_node = tmp_node_list
        result.append(node_value)

    return result


class Test(object):
    def __init__(self):
        self.name = "xxx"
        print('这是构造函数')

    def __del__(self):
        print('这是析构函数')

    def __getitem__(self, item):
        print("111", item)
        return self.__dict__.get(item, "100")

    def __getattr__(self, item):
        print("i am attr")
        return "2222"


demo = Test()
# print(dir(demo))
# print(demo['d'])
# print(demo['c'](user_id=2089278, a=2111))
print(demo.d)
print(demo['w'])
print(demo)