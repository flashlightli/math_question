class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        tmp_dic = {}
        if len(s1) != len(s2):
            return False
        else:
            for i in range(len(s1)):
                tmp_dic[s1[i]] = tmp_dic.get(s1[i]) + 1

            for i in range(len(s2)):
                tmp_dic[s2[2]] = tmp_dic.get(s2[i]) - 1

            for key, value in tmp_dic.items():
                if value != 0:
                    return False
            return True
