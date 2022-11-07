from typing import List
from math import sqrt

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:

        max_signal,res=-100,[0,0]
        for row in range(51):
            for col in range(51):
                cur_signal=0
                for item in towers:
                    dis=sqrt((item[0]-row)**2+(item[1]-col)**2)
                    if dis<=radius:
                        cur_signal+=int(item[2]/(1+dis))
                if cur_signal>max_signal:
                    max_signal,res=cur_signal,[row,col]

        return res
if __name__ == '__main__':
    towers = [[42,0,0]]
    radius = 7
    print(Solution().bestCoordinate(towers,radius))
