from typing import List

class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length=len(nums)
        ans=[]
        for left in range(length-1):
            for right in range(length-1,0,-1):
                start,end=left+1,right-1

                while start<end:
                    if nums[left]+nums[start]+nums[end]+nums[right]==target:
                        array=[nums[left],nums[start],nums[end],nums[right]]
                        if array not in ans:
                            ans.append(array)
                        start+=1
                        end-=1
                    elif nums[left]+nums[start]+nums[end]+nums[right]<target:
                        start+=1
                    else:
                        end-=1

        return ans


if __name__ == '__main__':
    nums = [0,0,0,0]
    target = 0
    print(Solution().fourSum(nums,target))
