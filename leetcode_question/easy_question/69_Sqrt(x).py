"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        res = self.recursion(int(x/2), x, x)

        return res

    def recursion(self, small, big, x):
        if small * small == x:
            return int(small)
        elif big * big == x:
            return int(big)

        elif big - small == 1 and small * small < x < big * big:
            return int(small)

        elif x > small * small:
            return self.recursion(min(small*2, big), max(small*2, big), x)
        elif x < big * big:
            return self.recursion(min(int(big/2), small), max(int(big/2), small), x)


test = Solution()
print(test.mySqrt(
    8
))