
class Solution:
    def countNumbersWithUniqueDigits(self, n: int):
        if n == 0:
            return 1
        result = 1
        for i in range(1, n+1):
            tmp = 1
            for j in range(1, i+1):
                if j == 1:
                    tmp = tmp * (10 - j)
                else:
                    tmp = tmp * (10 - j)
            result += result
        return result