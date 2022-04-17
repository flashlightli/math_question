class Solution:
    def myAtoi(self, s: str) -> int:
        # DFA算法 有限状态机
        table = {
            "start": ["start", "signed", "in_number", "end"],
            "signed": ["end", "end", "in_number", "end"],
            "in_number": ["end", "end", "in_number", "end"],
            "end": ['end', 'end', 'end', 'end'],
        }
        result = 0
        state = "start"
        sign = 1
        for i in s:
            state = table.get(state)[self.get_s_type(i)]
            if state == "in_number":
                result = result * 10 + int(i)
            elif state == "signed":
                sign = 1 if i == "+" else -1

        return max(sign * result, -2 ** 31) if sign == -1 else min(sign * result, 2 ** 31 - 1)

    def get_s_type(self, i):
        # 获取当前字符的类型
        if i == " ":
            return 0
        elif i in ("+", "-"):
            return 1
        elif i.isdigit():
            return 2
        else:
            return 3


test = Solution()
print(test.myAtoi(
    "   -42"
))