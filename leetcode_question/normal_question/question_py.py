"""
函数默认参数
因为默认列表只在函数被创建的那一刻创建一次

"""


def extend_list(value, demo_list=[]):
    demo_list.append(value)
    return demo_list

# 如果函数改成这样, list1 list3 就不会共用一个list了
# def extend_list(value, demo_list=[]):
#     if not demo_list:
#         demo_list = []
#     demo_list.append(value)
#     return demo_list

list_1 = extend_list(10)
list_2 = extend_list(20, [])
list_3 = extend_list(30)
print("list1==", list_1)
print("list2==", list_2)
print("list3==", list_3)


"""
copy
是因为  [[]] * 10 导致[]引用的是同一个列表
"""
demo_list = [[]] * 10
demo_list[0].append(10)
demo_list[1].append(20)
demo_list.append(30)
print(demo_list)
# [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]


"""
解决闭包问题
"""


def multipilers():
    return [lambda x: i * x for i in range(4)]


print([f(2) for f in multipilers()])


# 使用生成器
def multipilers_yield():
    for i in range(4):
        yield lambda x:i * x


print([f(2) for f in multipilers_yield()])


def multipilers_default():
    return [lambda x, i=i: i * x for i in range(4)]


print([f(2) for f in multipilers_default()])





