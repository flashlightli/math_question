"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def generate(self, numRows: int):
        # 40MS 13.7MB
        result = [[1], [1, 1]]
        if numRows <= 2:
            return result[:numRows]

        for i in range(2, numRows):
            tmp = [0] + result[-1] + [0]
            result.append([(tmp[j - 1] + tmp[j]) for j in range(1, i + 1)] + [1])

        return result


test = Solution()
print(test.generate(
    5
))