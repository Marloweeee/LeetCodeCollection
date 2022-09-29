from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=dict()
        for i,num in enumerate(nums):
            if target-num in res:
                return [res[target-num],i]
            res[num]=i
        print(res)
        return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s=Solution()
    print(s.twoSum(nums=nums,target=target))