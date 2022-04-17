class Solution:
    def firstMissingPositive(self, nums) -> int:
        # 置换 思路就是把循环到的数字置换到指定位置 那么不符合规范的数字/不符合逻辑的数字就是目标值
        len_nums = len(nums)
        for index, value in enumerate(nums):
            while 1 <= nums[index] <= len_nums and nums[nums[index] - 1] != nums[index]:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
            print("===")

        for index, value in enumerate(nums):
            if nums[index] != (index + 1):
                return index + 1

        return nums[-1] + 1


test = Solution()
print(test.firstMissingPositive(
    [3,4,-1,1]
))
