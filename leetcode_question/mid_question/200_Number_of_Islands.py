"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
11110
11010
11000
00000
输出: 1
示例 2:

输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numIslands(self, grid) -> int:
        # 72ms 14.3MB
        # DFS 深度优先算法
        if not grid:
            return 0

        result = 0
        for i in range(len(grid)):
            for j in grid[i]:
                if grid[i][j] == "1":
                    self.reset_arr(i, j, grid)
                    result += 1

        return result

    def reset_arr(self, i, j, grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
            pass

        grid[i][j] = '0'
        self.reset_arr(grid, i + 1, j)
        self.reset_arr(grid, i - 1, j)
        self.reset_arr(grid, i, j + 1)
        self.reset_arr(grid, i, j - 1)
