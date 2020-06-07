"""
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。

示例1
输入
复制
5 7
输出
复制
35
"""


def get_small_num(a, b):

    if a >= b:
        small = a
    else:
        small = b

    while True:
        if small % a == 0 and small % b == 0:
            break

        small += 1
    print(small)
    return small
