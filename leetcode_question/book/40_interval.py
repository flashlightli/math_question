"""
有n项工作, 每项工作在si时间开始,在ti项时间结束, 对于每项工作,你都可以选择参与,如果选择参与,那么自始至终都必须全程参与,此外,参与工作的时间段不能重叠,
即使是开始的瞬间和结束的瞬间也是不允许重叠的
你的目标是参与尽可能多的工作,那么最多能参与多少项工作呢?
n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]
"""


def get_max_work_count(n, s, t):
    # 按照结束时间的优先级排序 再按照开始时间优先级排序
    max_count = 0
    curr = 0
    tmp = []
    for i in range(n):
        tmp.append((s[i], t[i]))

    new_tmp = sorted(tmp, key=lambda x: (x[1], x[0]))
    for item in new_tmp:
        if not curr:
            max_count += 1
            curr = item[1]
            continue

        if item[0] > curr:
            max_count += 1
            curr = item[1]
            continue

    return max_count


get_max_work_count(
    5,
    [1,2,4,6,8],
    [3,5,7,9,10]
)