class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 基本的乘式计算
        if num2 == "0" or num1 == "0":
            return "0"

        list_a, list_b = list(num1), list(num2)
        total_arr = [0] * (len(num1) + len(num2))
        for index_i, value_i in enumerate(list_a):
            for index_j, value_j in enumerate(list_b):
                total_arr[index_i + index_j + 1] += int(value_i) * int(value_j)
                print(int(value_i) * int(value_j))

        for i in range(len(num1) + len(num2) - 1, 0, -1):
            total_arr[i - 1] += total_arr[i] // 10
            total_arr[i] %= 10

        index = 1 if total_arr[0] == 0 else 0
        ans = "".join(str(x) for x in total_arr[index:])
        return ans


test = Solution()
print(test.multiply(
    "123", "0"
))