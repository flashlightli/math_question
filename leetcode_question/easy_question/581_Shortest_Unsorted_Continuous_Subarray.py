"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
"""


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        num_len = len(nums)
        if num_len <= 1:
            return 0

        min_index = 0
        right = 0
        min_value = nums[0]
        for i in range(num_len):
            if nums[i] > nums[i + 1]:
                min_index = i
            else:
                num_len

        max_index = len(nums) - 1
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 1]:
                max_index = i
                break

        return max_index - min_index