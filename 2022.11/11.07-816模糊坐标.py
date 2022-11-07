from typing import List
from itertools import product
class Solution:

    def get_pos(self,num:str):
        res=[]
        if num[0]!='0' or num=='0':
            res.append(num)

        for i in range(1,len(num)):
            if i!=1 and num[0]=='0' or num[-1]=='0':
                continue
            res.append(num[:i]+'.'+num[i:])

        return res



    def ambiguousCoordinates(self, s: str) -> List[str]:

        s=s[1:-1]
        ans=[]
        for idx in range(1,len(s)):
            l=self.get_pos(s[:idx])
            if len(l)==0:
                continue

            r=self.get_pos(s[idx:])
            if len(r)==0:
                continue

            for i,j in product(l,r):
                ans.append('('+i+','+j+')')
        return ans

if __name__ == '__main__':

    print(Solution().ambiguousCoordinates('(00123)'))




