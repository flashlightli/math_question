class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        total = None
        arr = []
        for i in range(n):
            if total:
                total = total ^ (i * 2 + start)
            else:
                total = i * 2 + start
            arr.append(i * 2 + start)
        print(arr)
        return total


test = Solution()
print(test.xorOperation(
    10, 3
))