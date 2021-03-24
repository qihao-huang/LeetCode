# https://leetcode-cn.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        col_0_flag = any(matrix[i][0] == 0 for i in range(m))
        row_0_flag = any(matrix[0][i] == 0 for i in range(n))

        # 第 0 列， 第 0 行可以作为 [i,j] 的指示存储
        # 例如，如果 [i,j] 为 0， 那么 [0, j], [i, 0] 可以置 0 
        # 再次遍历矩阵，通过判断 [0, j], [i, 0] 去把该行，该列置 0
        # 这样的话就不需要一个额外的矩阵去 for i,j 遍历是否为 0 了

        # 注意是从 1 开始的。 
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0 

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col_0_flag:
            for i in range(m):
                matrix[i][0] = 0

        if row_0_flag:
            for j in range(n):
                matrix[0][j] = 0