class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        3行
        第一行:
        P	i * (3-1) - 1
        第二行:
        A	i * (3 - 2) - 1(上)
        第三行:
        Y   i * (3 - 1) - 1


        4行
        第一行:
        1	2 * (4-1) - 1  2 * (4 - 1) - 1
        第二行:	   已有行数      第几行
        2   2 * (4-2) - 1  2 * (2行 - 1) - 1
        第三行:
        3   2 * (4-3) - 1  2 * (3行 - 1) - 1
        最后:
        4   2 * (4 - 1) - 1
        """
        result = ""
        if not s:
            return result

        if numRows <= 1:
            return s

        list_s = list(s)
        for i in range(1, numRows+1):
            inner_i = i - 1
            dir = "up"
            while inner_i < len(list_s):
                print(inner_i, result)
                if i in (1, numRows):
                    result += list_s[inner_i]
                    inner_i += 2 * (numRows - 1)
                else:
                    result += list_s[inner_i]
                    if dir == "up":
                        inner_i += 2 * (numRows - i)
                        dir = "down"
                    else:
                        inner_i += 2 * (i - 1)
                        dir = "up"
        return result


test = Solution()
print(test.convert(
    "A", 1
))