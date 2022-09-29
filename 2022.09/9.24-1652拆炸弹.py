from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        length,ans=len(code),[]
        if k==0:
            return [0 for _ in range(length)]
        elif k>0:
            for idx in range(length):
                sum_num=0
                for i in range(idx+1,idx+1+k):
                    sum_num+=code[i%length]
                ans.append(sum_num)
        else:
            for idx in range(length):
                sum_num=0
                for i in range(idx-1,idx-1+k,-1):
                    sum_num+=code[i%length]
                ans.append(sum_num)
        return ans


if __name__ == '__main__':
    code = [2,4,9,3]
    k = 0
    print(Solution().decrypt(code,k))