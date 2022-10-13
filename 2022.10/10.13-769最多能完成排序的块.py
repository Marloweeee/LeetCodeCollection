from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        max_num,res=0,0

        for idx in range(len(arr)):
            max_num=max(max_num,arr[idx])
            if max_num==idx:
                res+=1
        return res

if __name__ == '__main__':
    print(Solution().maxChunksToSorted([1,0,2,3,4]))