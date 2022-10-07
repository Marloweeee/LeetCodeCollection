from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        left,right,sum=0,1,[nums[0] for i in range(len(nums))]

        while left<len(nums) and right<len(nums):
            if nums[right]>nums[left]:
                sum[right],left,right=sum[right-1]+nums[right],right,right+1
            else:
                sum[right],left,right=nums[right],right,right+1

        return max(sum)

if __name__ == '__main__':
    print(Solution().maxAscendingSum([100]))
