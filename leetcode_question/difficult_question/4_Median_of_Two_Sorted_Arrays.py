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
    def findMedianSortedArrays(self, nums1, nums2):
        # 转变成求第K小的元素
        is_single = len(nums1 + nums2) % 2
        if is_single:
            return self.findk(nums1, nums2, len(nums1 + nums2 + [0]) // 2)
        else:
            return (self.findk(nums1, nums2, len(nums1 + nums2) // 2) + self.findk(nums1, nums2, len(nums1 + nums2) // 2 + 1)) / 2

    def findk(self, nums1, nums2, k):
        # 以K为长度的二分查找
        p1, p2 = 0, 0
        while True:
            if len(nums1) == p1:
                return nums2[p2 + k - 1]

            if len(nums2) == p2:
                return nums1[p1 + k - 1]

            if k == 1:
                return min(nums1[p1],  nums2[p2])

            new_p1 = min(len(nums1) - 1, p1 + k // 2 - 1)   # 每个数组 K/2 的范围查找
            new_p2 = min(len(nums2) - 1, p2 + k // 2 - 1)
            if nums1[new_p1] <= nums2[new_p2]:
                k = k - (new_p1 - p1 + 1)   # K去掉小于中位数的个数
                p1 = new_p1 + 1             # 去掉的包括new_p1 所以p1要 + 1
            else:
                k = k - (new_p2 - p2 + 1)
                p2 = new_p2 + 1




test = Solution()
print(test.findMedianSortedArrays(
    [1, 2], [3, 4]
))
