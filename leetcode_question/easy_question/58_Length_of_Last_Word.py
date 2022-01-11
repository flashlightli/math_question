"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

 

示例:

输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 48ms 13.5MB
        s = s.strip()
        s_len, last_len = len(s), 0
        for i in range(s_len-1, -1, -1):
            if s[i] == " ":
                return s_len - i - 1
            last_len += 1

        return last_len

    def lengthOfLastWord_2(self, s: str) -> int:
        # 32MS 13.7MB
        s = s.split()
        return len(s[-1]) if s else 0

    def lengthOfLastWord_3(self, s: str) -> int:
        # 40MS 13.7MB
        if not s:
            return 0
        count = 0
        flag = 0
        for i in s[::-1]:
            if i is " " and flag == 0:
                continue
            if i is not " ":
                count += 1
                flag = 1
            else:
                break
        return count


"""
error_demo
"a "
"""

test = Solution()
print(test.lengthOfLastWord(
    "H"
))