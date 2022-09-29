from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return [-1,-1]

        def search(nums,target):
            left,right=0,len(nums)-1
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return left

        a=search(nums,target)
        b=search(nums,target+1)

        if a==len(nums) or nums[a]!=target :
            return [-1,-1]
        return [a,b-1]

if __name__ == '__main__':
    nums,target=[5,7,7,8,8,10], 10
    print(Solution().searchRange(nums,target))

