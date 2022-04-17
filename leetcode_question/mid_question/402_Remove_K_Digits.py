class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # 栈的知识
        remain = len(num) - k
        for i in num:
            # 数字从左到右 最左边的数字小 数字整体才会小
            # 从左到右遍历 比栈最后一个数字小的话替换栈最后一个数字 可移除的个数减一 直到移除的数字达到限制
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        return "".join(stack[:remain]).lstrip("0") or "0"


a = Solution()
print(a.removeKdigits("1432019", 3))