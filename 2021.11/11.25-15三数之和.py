from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []

        nums.sort(reverse=False)

        ans=[]
        for i in range(len(nums)):
            if nums[i]>0:
                continue
            left,right=i+1,len(nums)-1
            while(left<right):
                if nums[i]+nums[left]+nums[right]>0:
                    # print('>0', nums[i], nums[left], nums[right], nums[i] + nums[left] + nums[right])
                    right-=1

                elif nums[i]+nums[left]+nums[right]<0:
                    # print('<0', nums[i], nums[left], nums[right], nums[i] + nums[left] + nums[right])
                    left+=1

                else:
                    if [nums[i],nums[left],nums[right]] not in ans:
                        ans.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))