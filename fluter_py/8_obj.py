# ==比较的是值 is比较的是比较具体的标识  is运算符要比==快
charles = {"name": "li", "age": 12}
alex = {"name": "li", "age": 12}
print(alex == charles)
print(alex is charles)


# 引用默认是浅复制
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)

l1.append(100)
l1[1].remove(55)
l2[2] += (10, 11)
print("l1=====", l1)
print("l2=====", l2)


# 不要使用可变类型作为参数的默认值
class HauntedBus(object):

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['alice', 'bill'])
bus1.pick("li")
bus1.drop('bill')
print("bus1==", bus1.passengers)

bus2 = HauntedBus()
bus2.pick("zhe")
print("bus1==", bus1.passengers)
print("bus2==", bus2.passengers)
print(HauntedBus.__init__.__defaults__)     # __init__等于空list导致passengers绑定在了class这个属性上

bus3 = HauntedBus()
print("bus3==", bus3.passengers)    # 没有指定初始乘客的HauntedBus实例会共享同一个乘客列表


# 正确的修改 因为list是可变对象 __init__操作时不把可变对象当做默认值

class HauntedBus(object):

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers


# 垃圾回收 CPython 当引用次数为0时会将该对象销毁
import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print("Gone with the wind")


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)      # s2还没有消除对s1的引用后
s2 = 'www'
print(ender.alive)      # s2消除对s1的引用后 s1没有任何对象引用 会被回收


# 弱引用  不对增加对象的引用次数
a_set = {0, 1}
wref = weakref.ref(a_set)       # 创建弱引用对象
print(wref())


