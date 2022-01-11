"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def threeSum(self, nums):
        # 1068ms 16.2MB
        # 双指针  重点在去重
        result = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                return result
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] + target == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    # 去重
                    while start < end and nums[start] == nums[start + 1]:
                        start = start + 1
                    while start < end and nums[end] == nums[end - 1]:
                        end = end - 1
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] + target > 0:
                    end -= 1
                elif nums[start] + nums[end] + target < 0:
                    start += 1

        return result


test = Solution()
print(test.threeSum(
    [-2,0,0,2,2]
))