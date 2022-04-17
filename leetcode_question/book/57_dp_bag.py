"""
背包问题
有n个重量和价值分别为wi vi的物品, 从这些物品中挑选出总重量不超过W的物品,求所有挑选方案中价值总和的最大值
PS: 在这里, 每种物品可以挑选多件
n = 3
things_list = [(3,4),(4,5),(2,3)]
w = 7
"""


def get_max_value(n, w, thing_list=[]):
    # 普通DP算法
    tmp = []
    for i in range(n + 1):
        curr = []
        for j in range(w + 1):
            curr.append(0)
        tmp.append(curr)

    for i in range(i):
        for j in range(w):
            for k in range(len(thing_list)):
                if 
