class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        temp_dict = {key: 0 for key in wordList}
        all_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        temp_list = [beginWord]
        deep, word_len = 0, len(beginWord)
        while temp_list:
            new_temp_list = []
            for word in temp_list:
                for letter in all_letter:
                    for i in range(word_len):
                        if word == (word[:i] + letter + word[i+1:]):
                            continue
                        if (word[:i] + letter + word[i+1:]) in temp_dict:
                            if (word[:i] + letter + word[i + 1:]) == endWord:
                                deep += 2
                                return deep
                            new_temp_list.append(word[:i] + letter + word[i+1:])
                        else:
                            continue
            print(new_temp_list)
            for item in new_temp_list:
                temp_dict.pop(item)
            temp_list = new_temp_list
            deep += 1

        return 0


a = Solution()
a.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log"])