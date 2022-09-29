# coding=utf-8
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res,track=[],[]
        def backtrack(nums,start,track):
            res.append(track)

            for idx in range(start,len(nums)):
                print("当前的索引：{}，回溯数组：{}".format(idx, track))
                backtrack(nums,idx+1,track+[nums[idx]])
                
            return
        backtrack(nums,0,track)
        return res


print(Solution().subsets([1,2,3]))