from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        totle_step=0

        for op in logs:

            # remove to father dir
            if totle_step>0 and op=='../':
                totle_step-=1


            # make a new dir
            if op!='../' and op!='./':
                totle_step+=1

        return totle_step

if __name__ == '__main__':
    logs = ["d1/","d2/","../","d21/","./"]
    print(Solution().minOperations(logs))
