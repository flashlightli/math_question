"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 52ms 13.7MB
        loop_num = max(len(a), len(b)) + 1
        has_carry, result = 0, ""
        a, b = a.zfill(loop_num), b.zfill(loop_num)
        for i in range(-1, -loop_num, -1):
            if int(a[i]) + int(b[i]) + has_carry >= 2:
                result = str(int(a[i]) + int(b[i]) + has_carry - 2) + result
                has_carry = 1
            else:
                result = str(int(a[i]) + int(b[i]) + has_carry) + result
                has_carry = 0

        if has_carry == 1:
            result = "1" + result

        return result

    def addBinary_2(self, a: str, b: str) -> str:
        # 40ms 13.7MB
        x, y = int(a, 2), int(b, 2)
        # y其实是进位  ^---异或   &--都为1才为1
        while y:
            print(x, y, bin(x)[2:], bin(y)[2:])
            x, y = x ^ y, (x & y) << 1
        print(x, y, bin(x)[2:], bin(y)[2:])
        return bin(x)[2:]


test = Solution()
print(test.addBinary_2(
    "1", "111"
))
