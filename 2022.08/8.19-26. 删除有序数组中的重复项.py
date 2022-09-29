from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx,num_loc=0,0
        while idx<len(nums):
            if nums[idx]==nums[num_loc]:
                idx+=1
            else:
                num_loc+=1
                nums[num_loc]=nums[idx]
                idx+=1
        return num_loc+1
if __name__ == '__main__':
    nums=[0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))

