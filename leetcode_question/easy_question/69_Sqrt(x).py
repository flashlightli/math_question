"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # 40ms  13.5MB  每次比较中间元素调整范围
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            print(mid)

            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


test = Solution()
print(test.mySqrt(
    40
))