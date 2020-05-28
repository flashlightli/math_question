"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minPathSum(self, grid) -> int:
        path_sum = []

        for index_i, i in enumerate(grid):
            path_sum.append([])
            for index_j, j in enumerate(grid[i]):
                if index_i == 0 and index_j == 0:
                    path_sum[index_i].append(j)

                if index_i != 0 and index_j == 0:
                    path_sum[index_i].append(path_sum[index_i][-1] + j)

                if index_j != 0 and index_i == 0:
                    path_sum[index_i].append(path_sum[0][index_j] + j)

                if index_j and index_i:
                    path_sum[index_i].append(min(path_sum[index_i-1][j] + j, path_sum[index_i][index_j-1] + j))

        return path_sum[-1][-1]


test = Solution()
print(test.minPathSum(
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
))