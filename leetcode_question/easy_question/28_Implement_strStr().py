"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 52ms  13.8MB  字符串切片
        if not needle:
            return 0

        haystack = haystack.replace(needle, ",")
        if "," not in haystack:
            return -1

        return haystack.index(",")

    def strStr_2(self, haystack: str, needle: str) -> int:
        # 40ms  13.7MB
        hay_len, need_len = len(haystack), len(needle)
        for i in range(0, len(haystack) - need_len + 1):
            if haystack[i: i+need_len] == needle:
                return i

        return -1

    def strStr_3(self, haystack: str, needle: str) -> int:
        # KMP算法
        pass


test = Solution()
print(test.strStr(
    haystack = "aaaaa", needle = "bba"
))
