class Solution:
    def wordBreak(self, s, wordDict):
        word_dic = {i: 0 for i in wordDict}
        all_possible = {i: [] for i in range(1, len(s)+1)}
        for end_index in range(len(s)):
            if s[:end_index + 1] in word_dic:
                all_possible[end_index+1].append([s[0: end_index]])
            for mid_index in range(0, end_index + 1):
                if s[mid_index: end_index + 1] in word_dic:
                    all_possible = self.handle_part(s, mid_index, end_index+1, all_possible)
                    print(all_possible)

        print(all_possible)
        result = [" ".join(i) for i in all_possible.get(len(s))]
        print(result)
        return result

    def handle_part(self, s, mid_index, end_index, all_possible):
        print(mid_index, end_index)
        if all_possible.get(mid_index):
            temp = all_possible.get(mid_index)
            for i in temp:
                import copy
                temp_i = copy.deepcopy(i)
                temp_i.extend([s[mid_index: end_index]])
                all_possible[end_index].append(temp_i)

        return all_possible


a = Solution()
a.wordBreak("pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
            )