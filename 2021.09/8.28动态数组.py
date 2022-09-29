from typing import List
class Solution(object):
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums==[]:
            return '[]'
        # sum=[0 for i in range(len(nums))]
        # sum[0]+=nums[0]
        # for i in range(1,len(nums)):
        #     sum[i]=sum[i-1]+nums[i]
        # return sum
        for i in range(1,len(nums)):
            # print("{}+{}=".format(nums[i-1],nums[i]),end="")
            nums[i]=nums[i-1]+nums[i]
            # print(nums[i])
        return nums
if __name__ == '__main__':
    nums=[3,1,2,10,1]
    s=Solution()
    print(s.runningSum(nums))