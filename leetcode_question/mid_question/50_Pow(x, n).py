"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 44ms  13.7MB
        # 递归调用 小于0一开始就做判断转为大于0的
        def calander(x, n):
            if n == 1:
                return x

            if n % 2:
                number = calander(x, n // 2)
                return number * number * x
            else:
                number = calander(x, n // 2)
                return number * number

        if n == 0:
            return 1

        return calander(x, n) if n > 0 else 1 / calander(x, -n)


test = Solution()
print(test.myPow(
    2, -2
))