"""
给定整数a1, a2, a3, a4..., 判断是否可以从中选出若干数, 使他们的和恰好为k
输入:
n=4
a = [1,2,4,7]
k=13
输出:
Yes
"""


def get_sum(nums, k, curr=0, curr_sum=0):
    if curr >= len(nums):
        return False

    if nums[curr] + curr_sum == k:
        return True
    else:
        return get_sum(nums, k, curr + 1, curr_sum + nums[curr]) | get_sum(nums, k, curr + 1, curr_sum)


print(get_sum([1, 2, 4, 7], 15, curr=0, curr_sum=0))