"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"
输出:
[0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findAnagrams(self, s: str, p: str):
        # 112ms 14.7MB
        # 滑动窗口
        len_p = len(p)
        result = []

        p_dict = {}
        for i in p:
            p_dict[i] = p_dict[i] + 1 if i in p_dict else 1

        print(p_dict)
        left, right = 0, 0
        tmp_dict = {}
        while right < len(s):
            if s[right] not in p_dict:
                left, right = right + 1, right + 1
                tmp_dict = {}
            else:
                tmp_dict[s[right]] = tmp_dict.get(s[right], 0) + 1
                print(tmp_dict)
                if right - left + 1 == len_p:
                    if tmp_dict == p_dict:
                        result.append(right)
                    tmp_dict[s[left]] -= 1
                    left += 1
                right += 1

        return result


test = Solution()
print(test.findAnagrams(
    "cbaebabacd", "abc"
))