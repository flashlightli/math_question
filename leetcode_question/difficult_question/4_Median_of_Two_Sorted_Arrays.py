"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if len(nums1) > len(nums2):
            short_nums, long_nums = nums2, nums1
            short_nums_len, long_nums_len = len(nums2), len(nums1)
        else:
            short_nums, long_nums = nums1, nums2
            short_nums_len, long_nums_len = len(nums1), len(nums2)

        short_mid = short_nums_len // 2
        long_mid = long_nums_len // 2
        while True:
            if short_nums[short_mid] == long_nums[long_mid]:
                return short_nums[short_mid]
            elif short_nums[short_mid] > long_nums[long_mid]:
                short_mid -= 1
                long_mid += 1
            elif short_nums[short_mid] < long_nums[long_mid]:
                short_mid += 1
                long_mid -= 1

            if short_nums[short_mid] < long_nums[long_mid + 1] and short_nums[short_mid + 1] > long_nums[long_mid]:
                if (short_nums_len + long_nums_len) % 2:
                    return short_nums[short_mid] if short_nums[short_mid] <= long_nums[long_mid] else long_nums[long_mid]
                else:
                    sums = min(short_nums[short_mid + 1], long_nums[long_mid + 1]) + max(short_nums[short_mid], long_nums[long_mid])
                    return sums / 2


test = Solution()
print(test.findMedianSortedArrays(
    [1, 2, 5], [3, 4, 6]
))
