from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row,col=len(matrix),len(matrix[0])
        row_flag,col_flag=[0]*row,[0]*col
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_flag[i]=col_flag[j]=1
        for i in range(row):
            for j in range(col):
                if row_flag[i] or col_flag[j]:
                    matrix[i][j]=0






if __name__ == '__main__':
    mat=[
          [1,1,1],
          [1,0,1],
          [1,1,1],
        ]

    Solution().setZeroes(mat)