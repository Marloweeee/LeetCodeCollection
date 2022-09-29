from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # print(nums)

        dis=1000000
        ans=nums[0]+nums[1]+nums[2]
        diff=target-ans
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while(l<r and diff!=0):
                sum=nums[i]+nums[l]+nums[r]
                # print("nums[{}]+nums[{}]+nums[{}]={}+{}+{}={}".format(i,l,r,nums[i],nums[l],nums[r],sum))
                diff=(target-sum)
                if abs(diff)<dis:
                    ans=sum
                    dis=abs(diff)

                if diff>0:
                    l+=1
                else:
                    r-=1
        return (ans)

if __name__ == '__main__':

    nums = [1,1,1,0]
    target = -100
    print(Solution().threeSumClosest(nums,target))