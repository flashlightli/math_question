"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归 超时 暴力解法
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs_2(self, n: int) -> int:
        # 40ms 13.4MB
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3

        record_list = [0, 1, 2, 3]
        for i in range(4, n+1):
            record_list.append(record_list[i-1] + record_list[i-2])

        return record_list[-1]

    def climbStairs_3(self, n: int) -> int:
        # 20ms 13.6MB
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 1, 2
        for i in range(3, n+1):
            first, second = second, first + second

        return second


test = Solution()
print(test.climbStairs_3(
    44
))

