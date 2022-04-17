"""
直线上有N个点, 点i的位置是Xi, 从这N个点中选择若干个, 给他们加上标记,对每一个点,其距离为R以内的区域里必须带有标记的点(自己本身带有标记, 可以认为与
其距离为0的地方带有一个标记的点).在满足这个条件的情况下,希望能为尽可能少的点添加标记, 请问至少要有多少点被加上标记.
N=6 R=10
X= [1,7,15,20,30,50]

输出: 3
"""


def get_max_count(n, r, distance):
    # 贪心法 从左向右找到R覆盖的最多节点
    max_count = 0
    i = 0
    left, mid, right = 0, 0, 0
    while i < len(distance):
        if not left:
            left, mid, right = distance[i], distance[i], distance[i]
        # 向右找中间节点
        if left + r >= distance[i]:
            mid = distance[i]
        # 向右找到能覆盖的最右节点
        if mid + r >= distance[i]:
            right = distance[i]
        else:
            # 都找不到的话 当前节点之前的节点群 + 1 新的节点群建立
            max_count += 1
            left, mid, right = distance[i], distance[i], distance[i]

        i += 1
        print(left, mid, right, max_count)
    return max_count + 1


print(get_max_count(n=6, r=10, distance=[1, 7, 15, 20, 30, 50]))


