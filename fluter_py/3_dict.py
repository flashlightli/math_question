# 可散列的数据类型 不可变的数据类型
tt = (1, 2, (30, 40))
hash(tt)

tl = (1, 2, [30, 40])
# hash(tl) TypeError: unhashable type: 'list'

d_l = [30, 40]
tt = (1, 2, d_l)
# hash(tt) TypeError: unhashable type: 'list'

# 3-2
import sys
import re

print(sys.argv)     # 打印的该文件的路径 ['/Users/liyanzhe/Desktop/li/math_question/fluter_py/3_dict.py']
demo_dic = {}
demo_dic.setdefault("a", []).append(10)
print(demo_dic)

# 结果等同于如下  但是下面的代码需要进行两次键查询
if "b" not in demo_dic:
    demo_dic["b"] = []
demo_dic["b"].append(10)


import _collections
demo_dic = _collections.defaultdict(list)
print(demo_dic["w"], demo_dic)        # 返回默认设置的数据类型  其实调用的是内部的func  __missing__()只会在__getitem__被调用 d[k]


# 集合论  needles元素在haystack元素中出现的次数
needles = set([1, 2, 3])
haystack = set([2, 3, 4])
found = len(haystack & needles)
print(found)

print(frozenset(range(10)))
print(set({1 , 2, 3}).union([2, 3, 4], [4, 5, 6]))