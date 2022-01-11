"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heapsize = len(nums)

        def maxheap(a, i, length):
            l = 2 * i + 1
            r = 2 * i + 2
            large = i
            if l < length and a[l] > a[large]:
                large = l
            if r < length and a[r] > a[large]:
                large = r
            if large != i:
                a[large], a[i] = a[i], a[large]
                maxheap(a, large, length)

        for i in range(heapsize - 1, -1, -1):
            maxheap(nums, i, heapsize)

        for i in range(heapsize - 1, -1, -1):
            print(nums)
            nums[0], nums[i] = nums[i], nums[0]
            maxheap(nums, 0, i)
        return nums


test = Solution()
print(test.findKthLargest([3,6,2,4,1,8], 2))