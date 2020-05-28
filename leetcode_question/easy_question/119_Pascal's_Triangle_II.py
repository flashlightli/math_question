"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
优化到O(k)空间复杂度

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
"""


class Solution:
    def getRow(self, rowIndex: int):
        # 28MS 13.7MB
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        tmp = [1, 1]
        for i in range(2, rowIndex + 1):
            tmp = [0] + tmp + [0]
            tmp = [(tmp[j - 1] + tmp[j]) for j in range(1, i + 1)] + [1]

        return tmp


test = Solution()
print(test.getRow(
    5
))