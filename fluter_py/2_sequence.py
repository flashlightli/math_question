import array
import os
import collections
import bisect
import numpy

from random import random
from _collections import deque


symbols = 'jsjjax'
sy_list = [ord(i) for i in symbols]  # 返回对应的 ASCII 数值，或者 Unicode 数值
print(sy_list)

beyond_list = list(filter(lambda c: c > 110, map(ord, symbols)))
print(beyond_list)

colors = ["red", "yellow", "blue"]
sizes = ["S", "M", "L"]
shirt = [(color, size) for color in colors
                       for size in sizes]

print(shirt)

# 生成器表达式
# 初始化
t_list = tuple(ord(i) for i in symbols)
array_demo = array.array("I", t_list)
print(array_demo)

# 生成器表达式
for shirt in ((c, s) for c in colors for s in sizes):
    print(shirt)

# 元组拆包  路径解析出文件名
_, file_name = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(file_name)

a, b, *rest = [i for i in range(5)]  # *号可以放在任意一个位置
print(rest)

metro = [
    ("tokyo", 'JP', '36.933', (35, 123)),
    ("nanjing", 'JPD', '66.933', (65, 133))
]
fmt_str = "{:15} | {:9} | {:9}"
print('{:15} | {:^9} | {:^9}'.format('', 'qwe', 'asd'))
for name, cc, pop, (lat,lon) in metro:
    print(fmt_str.format(name, cc, lon, lat))

# 具名元组
Card = collections.namedtuple("Demo", ["width", 'length'])  # 第二个参数可以是空格隔开的字符串或者是字符串list
card = Card(12, (24, 34))  # 如果传递元组的话, 迭代对象类型须一致
print("===", card, card[1])
print("show fields", card._fields)

d_card = Card._make(('width_value', 'len_value'))
print(d_card._asdict())

# 文本解析切片
invoice = """
0.....6.............20.....26.....32
1991    demo_1         1      6
1992    demo_2         2      7 
"""
SKU = slice(0, 6)
DESC = slice(7, 20)
line_items = invoice.split("\n")[2:]
for item in line_items:
    print(item[SKU], item[DESC])

# 切片赋值
slice_list = [1, 2, 3, 4, 5]
slice_list[2:4] = [30, 40]      # 必须是list
print(slice_list)


# 对序列使用 + *
board = [['_'] * 3 for i in range(3)]
board[1][2] = 4
print(board)  # [['_', '_', '_'], ['_', '_', 4], ['_', '_', '_']]

# 注意点 引用
board = [['_'] * 3] * 3  # * 指向对同一个列表的引用
board[1][2] = 4
print(board)    # [['_', '_', 4], ['_', '_', 4], ['_', '_', 4]]

# **** 关键问题  不要把可变元素放入元组里面  增量赋值不是原子操作
a = (1, 2, [3, 4])
# a[2] += [5, 6]
print(a)
# 如果在shell里面运行 会发现a=(1, 2, [3, 4, 5, 6])

b = [3, 4]
w = (1, 2, b)
b += [5, 6]
print(w) # (1, 2, [3, 4, 5, 6])


# list里面的sort  不会创建一个list,所以返回None
un_sort_list = ["fejkjqf", "cacac", "caca", "fqwad"]
# un_sort_list.sort()
print(un_sort_list)

# sorted会创建一个新的list 原来的list不会被改变
sorted_list = sorted(un_sort_list)
print(sorted_list, un_sort_list)

print("根据长度排序", sorted(un_sort_list, key=len, reverse=True))
print("忽略大小写排序", sorted(un_sort_list, key=str.lower, reverse=True))

haystack = [1, 4, 5, 6, 10]
Needles = [2, 5, 6, 9]
for i in Needles:
    l_position = bisect.bisect_left(haystack, i)  # 5会放在haystack里面5的前面
    r_position = bisect.bisect_right(haystack, i)   # 5会放在haystack里面5的后面
    position = bisect.bisect(haystack, i)

    print(position, l_position, r_position, haystack)

bisect.insort_left(haystack, 7)    # 插入到左边
print(haystack)
bisect.insort_right(haystack, 7)    # 插入到右边
print(haystack)
bisect.insort(haystack, 7)
print(haystack)


# 浮点型数组创建-存入文件--从文件读取 tofile/fromfile读取写入文件很快
from array import array
flotes = array('d', (random() for i in range(10**7)))
print(flotes[-1])

# fp = open("flotes.bin", 'wb')
# flotes.tofile(fp)
# fp.close()
# flotes2 = array('d')
# fp = open("flotes.bin", "rb")
# flotes2.fromfile(fp, 10**7)
# fp.close()
# print(flotes2[-1])


# 内存视图 不复制原list  通过共享内存来实现
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
memv_oct = memv.cast("B")       # 转成了二进制
print(memv_oct.tolist())
memv_oct[5] = 4     # 把高位字节变成4
print(numbers)


# numpy的简单使用
a = numpy.arange(12)
print(a)
a.shape = 3, 4   # 变成3行4列的数组
print(a, "===", a[:, 1])
print("transpose====", a.transpose())


# 双向队列的简单使用
dq = deque(range(10), maxlen=10)
dq.rotate(3)
print(dq)
dq.appendleft(-1)
dq.extendleft([-3, -2])  # 因为有长度限制 新添加的元素会挤掉后面的元素
