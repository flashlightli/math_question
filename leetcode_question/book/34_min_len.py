"""
给定一个大小为N * M 的迷宫, 迷宫由通道和墙壁组成, 每一步可以向邻接的上下左右四格的通道移动,请求出从起点到终点所需的最小步数,
本题假定从起点一定可以移动到终点
N= 10 M = 10
"""


def get_min_len(n, m, maze):
    start_i, start_j = get_start(n, m, maze)
    tmp = [(start_i, start_j)]
    path_len = 0
    maze_tmp = [[0 for i in range(len(maze[0]))] for j in range(len(maze[0]))]
    while tmp:
        this_loop = []
        path_len += 1
        for item in tmp:
            if maze[item[0]][item[1]] in ("S", "."):
                print(item[0], item[1], maze_tmp)
                maze_tmp[item[0]][item[1]] = 1
                if (item[0] + 1) < len(maze) and maze_tmp[item[0] + 1][item[1]] != 1:
                    this_loop.append((item[0] + 1, item[1]))
                if (item[0] - 1) >= 0 and maze_tmp[item[0] - 1][item[1]] != 1:
                    this_loop.append((item[0] - 1, item[1]))
                if (item[1] - 1) >= 0 and maze_tmp[item[0]][item[1] - 1] != 1:
                    this_loop.append((item[0], item[1] - 1))
                if maze and (item[1] + 1) < len(maze[0]) and maze_tmp[item[0]][item[1] + 1] != 1:
                    this_loop.append((item[0], item[1] + 1))

            elif maze[item[0]][item[1]] in ("G", ):
                return path_len
        tmp = this_loop


def get_start(n, m, maze):
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "S":
                return i, j


print(get_min_len(
    10, 10,
    [
        ["#", "S", "#", "#", "#", "#", "#", "#", ".", "#"],
        [".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
        [".", "#", ".", "#", "#", ".", "#", "#", ".", "#"],
        [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        ["#", "#", ".", "#", "#", ".", "#", "#", "#", "#"],
        [".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
        [".", "#", "#", "#", "#", "#", "#", "#", ".", "#"],
        [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
        [".", "#", "#", "#", "#", ".", "#", "#", "#", "."],
        [".", ".", ".", ".", "#", ".", ".", ".", "G", "#"],
    ]
))