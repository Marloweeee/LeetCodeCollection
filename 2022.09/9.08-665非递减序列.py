from typing import List

class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:

        sum=0
        for idx in range(1,len(nums)):
            if nums[idx]>=nums[idx-1]:
                continue
            sum+=1
            if idx-2>=0 and nums[idx-2]>nums[idx]:
                nums[idx]=nums[idx-1]
            else:
                nums[idx-1]=nums[idx]

        if sum>1:
            return False
        return True
if __name__ == '__main__':
    print(Solution().checkPossibility([3,4,2,3]))