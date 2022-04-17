class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        all_rectangle = [[(0, 0, 0)] * cols] * rows
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == 0:
                    all_rectangle[i][j] = (0, 0, 0)
                else:
                    all_rectangle[i][j] = (
                        all_rectangle[i][j-1][0]+1,
                        min(all_rectangle[i-1][j-1][1]+1, all_rectangle[i-1][j-1][1]+1, all_rectangle[i-1][j-1][1]+1),
                        all_rectangle[i-1][j][2]+1
                    )

