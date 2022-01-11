"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
"""


class Solution:
    def maxSubArray(self, nums):
        # 44ms 14.2MB
        if not nums:
            return

        temp, max_value = nums[0], nums[0]
        for index in range(1, len(nums)):
            if temp > 0:
                temp += nums[index]
            else:
                temp = nums[index]
            max_value = max(max_value, temp)

        return max_value

    def maxSubArray_2(self, nums):
        # DP
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            # 下面为nums长度至少为2的情况
        res = nums[0]  # 先设定一个初始值（假设第一个数是可获得的最小值）
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])  # 更新后的nums[i]存储 以原始num[i]为结尾的子数组和的最大值
            res = max(res, nums[i])  # 更新最大值
        print(nums)
        return res

    def maxSubArray_3(self, nums):
        # 分治法
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray_3(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray_3(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)


"""
[-2,1]
[-1]
[-2, -1]
[-2,1,-3,4,-1,2,1,-5,4]
"""
test = Solution()
print(test.maxSubArray_2(
    [-2, -1]
))