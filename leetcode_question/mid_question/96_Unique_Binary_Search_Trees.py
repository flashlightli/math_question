"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # 44ms 13.7MB
        # 动态规划
        start_list = [0, 1, 2]
        if n <= 2:
            return start_list[n]

        for i in range(3, n+1):
            tmp = start_list[-1] * 2
            start, end = 1, i - 2
            while start <= end:
                base_times = 1 if start == end else 2
                tmp += (start_list[start] * start_list[end]) * base_times
                start += 1
                end -= 1

            start_list.append(tmp)

        return start_list[-1]


test = Solution()
print(test.numTrees(
    5
))