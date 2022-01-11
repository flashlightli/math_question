"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。


你能不将整数转为字符串来解决这个问题吗？
"""


class Solution:
    def isPalindrome(self, x):
        # 72ms 13.7MB
        if x == 0:
            return True

        if x < 0:
            return False

        x_list = list(str(x))   # list比对速度比较快
        reverse_list = x_list[::-1]
        if x_list == reverse_list:
            return True

        return False

    def isPalindrome_2(self, x):
        # 116ms 13.7MB 取余比对
        if x == 0:
            return True

        if x < 0:
            return False

        new = 0
        old = x
        while x > 0:
            tmp = x % 10
            new = new * 10 + tmp
            x //= 10

        return new == old

    def isPalindrome_3(self, x):
        # 回文一半和原字符串做比较
        if x == 0:
            return True

        if x < 0 or (x % 10) == 0:
            return False

        ans = 0
        while x > ans:
            ans = ans * 10 + x % 10
            x //= 10
        return x == ans or x == (ans // 10)


"""
error test demo:
"""
test = Solution()
print(test.isPalindrome_3(
    121
))