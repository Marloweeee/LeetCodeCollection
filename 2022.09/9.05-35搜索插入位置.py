from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target>nums[-1]:
            return len(nums)
        if target>nums[0] and target<nums[1]:
            return 1


        left,right=0,len(nums)-1


        while(left<=right):

            mid=(left+right)//2
            if target<=nums[mid]:
                ans=mid
                right=mid-1
            else:
                left=mid+1


        return ans

if __name__ == '__main__':
    nums,target=[1,2,4,5,9],3
    print(Solution().searchInsert(nums,target))