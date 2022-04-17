"""
将一块很长的木板切割成N块, 准备切成木板的长度为L1, L2...Ln, 未切割前木板的长度恰好为切割后木板长度的总和, 每次切割木板时, 需要的开销为这块木板的长度
.例如: 长度为21的木板要切割成5,8,8的三块木板,长21的木板切成长为13 8的开销为21,再将长度为13的木板切成5 8的开销为13, 于是总开销为34, 请求出按照目标要求
将木板切割完的最小开销是多少
"""


def get_min_expenses(n, len_list):
    # 贪心算法
    # 优先队列，每次都把最小的两个相加再入队，最后队列里只剩一个数时就是所要求的答案。
    len_list = sorted(len_list, reverse=True)
    min_expense = 0
    for i in range(n - 1):
        min_expense += len_list[i] + sum(len_list[i+1:])

    return min_expense


print(get_min_expenses(3, [8, 5, 8]))