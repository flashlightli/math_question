"""
有N条绳子 长度分别为Li0,如果从他们中切割出K条长度相同的生子的话,这K条绳子每条最长能有多长? (精确到小数点后两位)
二分搜索 求近似最优解
N=3
K=11
L=[8.02,7.43,4.57,5.39]

答案是2.00
"""


def get_sum(k_len, len_list, limit_len):
    total = 0
    for i in len_list:
        total += i // k_len
    return limit_len <= total


def get_k_len(n, k, len_list):
    min_len, max_len = 0.00, max(len_list) * 2
    for i in range(100):
        mid = (min_len + max_len) / 2
        if get_sum(mid, len_list, k):
            min_len = mid
        else:
            max_len = mid
        print(min_len, round(max_len, 3))

    print(min_len, round(max_len, 3))


#get_k_len(3, 11, [8.02, 7.43, 4.57, 5.39])



"""
N间牛舍,牛舍在一条直线,第i个牛舍在xi的位置,但是有M头牛经常互相攻击,求最大化两头牛的距离
N=5
M=3
x=[1,2,8,4,9]

距离是3(1,4,9) 的最短间隔是3
"""


def judge_distance(distance, new_x, m):
    last_location, total, curr_distance = new_x[0], 0, 0
    for i in range(new_x):
        if i - distance >= last_location:
            curr_distance = max(curr_distance, (i - last_location))
            last_location = i
            total += 1
    print("===")
    print(curr_distance)
    return total >= m, curr_distance


def get_max_distance(n, m, x):
    new_x = sorted(x)
    max_distance = new_x[1] - new_x[0]
    for i in range(m):
        result, curr_distance = judge_distance(max_distance, new_x, m)
        if result:
            max_distance = curr_distance
        else:
            print(max_distance)
            return max_distance


get_max_distance(5, 3, [1,2,8,4,9])



