class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [[1, 1]]

        total = 0
        for i in range(1, 32):
            dp.append([dp[i-1][0] + dp[i-1][1], dp[i-1][0]])

        print(dp, len(dp))
        a = list(bin(n)[2:])
        a.reverse()
        print(a, len(a))
        curr, pre = 0, -1
        for index, value in enumerate(a):
            if value == "1":
                total += dp[index][0]
            if pre == curr and curr == 1:
                break
            pre = curr
            if index == len(a) - 1:
                total += 1

        print(total)
        return total

Solution().findIntegers(20)
