"""
给定两个字符串 s1s2s3...sn和t1t2t3tn, 求这两个字符串的最长公共子序列的长度,
输入:
s = 'abcd' n = 4
t = 'bcde' m = 4
"""


def dp_longest_string(s, t):
    # 和背包问题一致
    s_len, t_len = len(s), len(t)
    tmp = []
    for i in range(s_len + 1):
        curr = []
        for j in range(t_len + 1):
            curr.append(0)
        tmp.append(curr)

    for i in range(s_len):
        for j in range(t_len):
            if s[i] == t[j]:
                tmp[i+1][j+1] = tmp[i][j] + 1
            else:
                tmp[i+1][j+1] = max(tmp[i+1][j], tmp[i][j+1])

    return tmp[-1][-1]


print(dp_longest_string("abcd", "bcde"))
