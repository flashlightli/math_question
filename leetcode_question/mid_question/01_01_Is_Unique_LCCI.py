class Solution:
    def isUnique(self, astr: str) -> bool:
        """
        实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
        位运算 找一个26个长度的数组 或者 一个26位的bit数字
        """
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mark & (1 << move_bit)) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True
