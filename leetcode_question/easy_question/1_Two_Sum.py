"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:
    def twoSum(self, nums, target):
        # 64 ms 15.7 MB
        if not nums:
            return

        nums_dict = {value: index for index, value in enumerate(nums)}
        nums, old_nums = sorted(nums), nums

        index, last = 0, len(nums) - 1
        while index < last:
            if nums[index] + nums[last] > target:
                last -= 1

            if nums[index] + nums[last] < target:
                index += 1

            if nums[index] + nums[last] == target:
                break

        if nums[index] + nums[last] == target:
            return [old_nums.index(nums[index]), nums_dict[nums[last]]]

        return

    def twoSum_2(self, nums, target):
        # 940ms 14.7 MB
        if not nums:
            return

        for index, value in enumerate(nums):
            if (target - nums[index]) in nums[(index+1):]:
                if index == nums.index(target - nums[index]):
                    import pdb
                    pdb.set_trace()
                    return [index, nums.index(target - nums[index], index+1)]

                return [index, nums.index(target - nums[index])]

        return

    def twoSum_3(self, nums, target):
        # 64ms  15MB
        if not nums:
            return

        nums_dict = {}
        for index, value in enumerate(nums):
            if (target - value) in nums_dict:
                return [nums_dict[target - value], index]

            nums_dict[value] = index


"""
error test demo:
twoSum([3, 2, 4], 6)
twoSum([3, 3], 6)
[2,5,5,11]
10
"""
test = Solution()
print(test.twoSum_3(
    [2, 5, 5, 11],
    10
))

"""
执行用时 :
64 ms
, 在所有 Python3 提交中击败了
56.61%
的用户
内存消耗 :
15.7 MB
, 在所有 Python3 提交中击败了
5.48%
的用户
"""
