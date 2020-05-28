"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution:
    def isValid(self, s):
        # 64ms 13.6MB
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    def isValid_2(self, s):
        # 32ms 13.7MB
        in_dict = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        out_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        tmp = []
        for i in s:
            if i in in_dict:
                tmp.append(in_dict[i])

            elif tmp and i in out_dict:
                if i != tmp.pop():
                    return False
            else:
                tmp.append(i)

        return True if not tmp else False


test = Solution()
print(test.isValid_2(
    "["
))
