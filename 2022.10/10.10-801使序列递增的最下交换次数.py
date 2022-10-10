from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        length=len(nums1)

        dp=[[100000,100000] for i in range(length)]
        dp[0]=[0,1]
        for idx in range(1,length):
            if nums1[idx]>nums1[idx-1] and nums2[idx]>nums2[idx-1]:
                dp[idx][0],dp[idx][1]=dp[idx-1][0],dp[idx-1][1]+1
            if nums1[idx]>nums2[idx-1] and nums2[idx]>nums1[idx-1]:
                dp[idx][0]=min(dp[idx][0],dp[idx-1][1])
                dp[idx][1]=min(dp[idx][1],dp[idx-1][0]+1)


        return min(dp[-1])


if __name__ == '__main__':
    nums1 = [1, 3, 5, 4]
    nums2 = [1, 2, 3, 7]
    print(Solution().minSwap(nums1,nums2))

