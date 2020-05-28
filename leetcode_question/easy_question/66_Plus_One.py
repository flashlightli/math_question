"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plus-one
"""


class Solution:
    def plusOne(self, digits):
        # 44ms 13.8MB
        new_list = [str(i) for i in digits]
        new_num = int("".join(new_list)) + 1
        return [int(i) for i in str(new_num)]

    def plusOne_2(self, digits):
        # 40ms 13.7MB 倒序
        num_len, new_list = len(digits) - 1, []
        flag = True
        for i in range(num_len, -1, -1):
            if flag:
                if (digits[i] + 1) == 10:
                    new_list = new_list + [0]
                else:
                    flag = False
                    new_list = [digits[i] + 1] + new_list
            else:
                flag = False
                new_list = [digits[i]] + new_list

        if flag:
            new_list = [1] + new_list

        return new_list


test = Solution()
print(test.plusOne_2(
    [1,2,3]
))