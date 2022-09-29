from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        loc=0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[loc]=nums[idx]
                loc+=1
        return loc

if __name__ == '__main__':
    print(Solution().removeElement([0,1,2,2,3,0,4,2],2))