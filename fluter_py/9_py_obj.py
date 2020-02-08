import datetime
from array import array


# page206
class Vector2d:
    typecode= 'd'       # 各个变量的精度
    __slots__ = ('__x', '__y')  # 会把存在__dict__字典里面的属性放入元组 减少内存的使用  使用场景:处理列表数据

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __format__(self, format_spec=''):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)

    def __hash__(self):     # 实现 hash 和 eq 方法实现散列
        return hash(self.x) ^ hash(self.y)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bytes__(self):
        return (bytes([ord(self.typecode)])
                + bytes(array(self.typecode, self)))


v1 = Vector2d(3, 4)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)


# format 基本操作
brl = 1 / 2.43
print(format(brl, '0.4f'))  # 小数点后4位
print(format(42, 'b'))  # 转换成二进制字符串
print(format(2/3, '.1%'))   # 百分号后一位
print(format(datetime.datetime.now(), '%H:%M:%S'))  # 时间的字符串输出
print(format(v1, '.2f'))            # 实例的字符串输出 实例定义了format方法
v2 = Vector2d(4, 3)
print(hash(v1), hash(v2))
print(len(bytes(v1)))   # 字节长度是17
# print(v1.__dict__)      # 名称改写 私有属性会加上类名存入实例的dict属性中


class ShortVector2d(Vector2d):
    typecode = 'f'      #


sv = ShortVector2d(1/11, 1/27)
print(len(bytes(sv)))       # 字节长度是9
