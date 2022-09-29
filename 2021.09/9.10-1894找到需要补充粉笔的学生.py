from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n=len(chalk)
        totle=sum(chalk)
        k%=totle
        idx=0
        while(k>=chalk[idx]):
            k-=chalk[idx]
            idx=(idx+1)%n
            # print(idx)
        return idx
if __name__ == '__main__':
    chalk,k=[97,20,100,23,27,33,31,69,72,27,51,7,97,38,88,21,4,68,29,56,24,72,70,84,2,99,14,34,3,40,74,74,4,83,71,25,62,69,12,37,12,89,10,15,30,82,13,39,10,70,98,63,99,62,25,37,80,81,17,86,80,32,71,18,83,28,89,57,16,74,91,65,100,70,25,72,21,13,75,28],810125956
    print(Solution().chalkReplacer(chalk,k))