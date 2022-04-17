class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        all_result = []
        for i in range(len_t+1):
            temp = []
            for j in range(len_s+1):
                temp.append(0)
            all_result.append(temp)

        for index_t, value_t in enumerate(t):
            for index_s, value_s in enumerate(s):
                if index_s < index_t:
                    all_result[index_t + 1][index_s + 1] = 0
                    continue

                if value_s == value_t:
                    all_result[index_t+1][index_s+1] = (all_result[index_t][index_s] + all_result[index_t+1][index_s]+ 1) if index_t == 0 else (all_result[index_t][index_s] + all_result[index_t+1][index_s])
                else:
                    all_result[index_t + 1][index_s + 1] = all_result[index_t+1][index_s]

        print(all_result)
        return all_result[-1][-1]


a = Solution()
print(a.numDistinct(s = "babgbag", t = "bag"))