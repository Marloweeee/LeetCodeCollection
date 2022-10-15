from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        for num in range(1,n+1):
            if num in target:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
            if num==target[-1]:
                break
        return res
if __name__ == '__main__':
    print(Solution().buildArray([1,2,],4))