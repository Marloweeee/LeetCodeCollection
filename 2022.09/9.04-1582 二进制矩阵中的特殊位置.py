from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        if mat==[]:
            return 0

        row_sum=[sum(row) for row in mat]
        col_sum=[sum(col) for col in zip(*mat)]
        res=0

        for row_num,row in enumerate(mat):
            for col_num,col in enumerate(row):
                if row_sum[row_num]==1 and col_sum[col_num]==1 and col==1:
                    res+=1

        return res

if __name__ == '__main__':

    mat = [[0, 0, 1],
           [0, 1, 0],
           [0, 0, 0]]
    A=[1,5,2,4]
    B=['1','5','2','4']
    C,D=zip(*sorted(zip(A,B)))
    print(C,D)

    print(list(zip(*mat)))
