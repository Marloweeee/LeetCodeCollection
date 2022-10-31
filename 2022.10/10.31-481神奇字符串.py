class Solution:
    def magicalString(self, n: int) -> int:

        if n<3:
            return 1

        res,idx=[1,2,2],2

        while len(res)<n:
            res+=[res[-1]^3]*res[idx]
            idx+=1

        return res[:n].count(1)






