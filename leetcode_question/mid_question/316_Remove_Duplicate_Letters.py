class Solution:
    def removeDuplicateLetters(self, s: str):
        tmp = {}
        result = []
        for index in range(len(s)):
            if s[index] not in tmp:
                result.append(s[index])
                tmp[s[index]] = 1
            else:
                while i
