class Solution:
    def countDigitOne(self, n: int) -> int:
        # 根据数字各位的位数进行计算
        if not n:
            return 0

        len_n = len(str(n))
        digit = len_n
        total = 0
        last_digit = 1
        for index, i in enumerate(str(n)):
            if i == '1':
                total += (10 ** (digit - index - 1)) * (0 if index == 0 else last_digit) + int(str(n)[index+1:] or 0) + 1
            elif i == '0':
                total += (10 ** (digit - index - 1)) * last_digit
            else:
                total += (10 ** (digit - index - 1)) * (1 if index == 0 else (last_digit + 1))
            last_digit = int(i) if index == 0 else (last_digit * 10 + int(i))

        return total


test = Solution()
print(test.countDigitOne(
    206
))