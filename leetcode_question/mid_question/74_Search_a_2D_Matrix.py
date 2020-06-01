"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # 二分法   44ms 13.6MB
        m = len(matrix)
        if not m:
            return False

        n = len(matrix[0])

        # 二分查找
        left, right = 0, m * n - 1
        while left <= right:
            curr_mid = (left + right) // 2
            mid_element = matrix[curr_mid // n][curr_mid % n]
            if mid_element == target:
                return True
            else:
                if mid_element > target:
                    right = curr_mid - 1
                else:
                    left = curr_mid + 1

        return False


test = Solution()
print(test.searchMatrix(
    [[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3
))