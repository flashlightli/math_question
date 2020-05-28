"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        # 52ms 14.4MB
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == target:
                return i

            if nums[j] == target:
                return j

            if nums[j] < target:
                return j + 1

            if nums[i] > target:
                return i

            if nums[i] < target < nums[j]:
                mid = (i + j) // 2
                if nums[mid] == target:
                    return mid
                if (j - i) == 1:
                    return i if nums[i] > target else j
                if nums[mid] < target:
                    i, j = mid, j
                    continue
                if nums[mid] > target:
                    i, j = i, mid
                    continue
        return i

    def searchInsert_2(self, nums, target: int) -> int:
        # 32ms 14.4MB
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


"""
[1], 0
[1,3], 3
"""
test = Solution()
print(test.searchInsert(
    [1], 2
))