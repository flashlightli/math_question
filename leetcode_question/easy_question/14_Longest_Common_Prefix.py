"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        # 40ms 13.7MB
        common_str = ""
        if not strs:
            return common_str

        min_len = len(min(strs))
        for i in range(min_len):
            common_str += strs[0][i:i+1]
            for s in strs[1:]:
                if s[:i+1] != common_str:
                    return common_str[:i]

        return common_str

    def longestCommonPrefix_2(self, strs):
        # 40ms 13.7MB
        # max min是可以比较ASCII码的 如果前几位的字符一样 那么ASCII码的前几位也一样
        #
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    def longestCommonPrefix_3(self, strs):
        # 36ms 13.8MB
        if not strs: return ""
        ss = list(map(set, zip(*strs)))     # 会把list变成二维数组 并且去重
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


test = Solution()
print(test.longestCommonPrefix(
    ["dog","racecar","car"]
))