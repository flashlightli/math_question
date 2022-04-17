"""
有一个大小为N * M的园子, 雨后有了积水, 八连通的积水被认为是连接在一起的,请求出园子里共有多少水洼
N=10 M=12
w******ww
*ww*****W
**WWW***W
**WW***WW
*********
**ww*****
*********
输出=3
"""


def get_lake_count(n, m, lakes):
    # 遍历过的就把数组变成 非水洼
    # 使用Python注意i j 为 -1 的情况
    def dfs_search(i, j):
        if i >= len(lakes) or i < 0:
            return False

        if (lakes and len(lakes[0]) <= j) or j < 0 :
            return False

        if lakes[i][j] == "w":
            lakes[i][j] = "*"
            return dfs_search(i + 1, j + 1) | dfs_search(i - 1, j - 1) | dfs_search(i - 1, j) | dfs_search(i - 1,
                                                                                                           j + 1) | \
                   dfs_search(i, j - 1) | dfs_search(i, j + 1) | dfs_search(i + 1, j - 1) | dfs_search(i + 1, j) | True

        else:
            return False

    lake_count = 0
    for i in range(n):
        for j in range(m):
            lake_count += 1 if dfs_search(i, j) else 0

    return lake_count


print(get_lake_count(
    5, 5,
    [
        ["w", "*", "*", "*", "w"],
        ["*", "w", "w", "*", "w"],
        ["*", "w", "*", "*", "w"],
        ["*", "*", "*", "*", "*"],
        ["*", "w", "*", "*", "*"],
    ]
))