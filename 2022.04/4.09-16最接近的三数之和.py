from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(n):
            l,r=i+1,n-1
            while(l<r):
                sum=nums[i] + nums[l] + nums[r]
                if abs(sum-target)<abs(res-target):
                    res = sum
                if(res-target>0):
                    r-=1
                elif(res-target<0):
                    l+=1
                else:
                    return res
        return res


if __name__ == '__main__':
    nums=[-1,2,1,4]
    target=10
    print(Solution().threeSumClosest(nums,target))

