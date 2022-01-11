"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
输入: 123
输出: 321
"""


class Solution:
    def reverse(self, x):
        # 44ms 13.7MB
        if x == 0:
            return x

        symbol_num = 1 if x > 0 else -1
        x_list = list(str(x))

        x_list = x_list if symbol_num > 0 else x_list[1:]
        x_list.reverse()
        new_x_str = "".join(x_list)

        if -2 ** 31 < symbol_num * int(new_x_str) < 2 ** 31 - 1:
            return symbol_num * int(new_x_str)

        return 0


"""
error test demo:
1534236469 溢出需要check
"""
test = Solution()
print(test.reverse(
    0
))