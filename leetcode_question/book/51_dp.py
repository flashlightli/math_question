"""
背包问题
有n个重量和价值分别为wi vi的物品, 从这些物品中挑选出总重量不超过W的物品,求所有挑选方案中价值总和的最大值
n = 4
{w, v} = {(2,3), (1,2), (3,4), (2,3)}
w = 5

输出: 7 选0 1 3号物品
"""


def dp_bag(n, w, thing_list):
    # DP算法背包问题
    """
    画格子图
    A[i-1][j-wight]: i-1个数的物品 重量为 j-当前物品的重量
    当前的最大价值=max(上一个重量的最大值, A[i-1][j-wight] + 当前物品的value)
    """
    tmp = []
    for i in range(n+1):
        tmp.append([])
        for j in range(w+1):
            tmp[i].append(0)

    for index in range(1, n+1):
        curr_wight, curr_value = thing_list[index - 1]
        for wight in range(1, w+1):
            if curr_wight > wight:
                tmp[index][wight] = tmp[index - 1][wight]
            else:
                tmp[index][wight] = max(curr_value, (tmp[index - 1][wight - curr_wight] + curr_value))

    return tmp[-1][-1]


print(dp_bag(
    n=4, w=5,
    thing_list=[(2,3), (1,2), (3,4), (2,3)]
))

