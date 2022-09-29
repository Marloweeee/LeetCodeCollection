# coding=utf-8
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        # b区间所有数字均大于等于x，a区间所有数字小于x，而x与len(b)的值相等
        # 故：max(a)<len(b)<=min(b)

        nums.sort()
        length=len(nums)
        first_num=True

        if nums==[]:
            return -1


        for idx in range(length):
            if first_num:
                if length<=nums[0]:
                    return length
                first_num=False

            else:
                if nums[idx]>=length-idx and nums[idx-1] <length-idx:
                    return length-idx
        return -1



if __name__ == '__main__':
    nums=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    print(Solution().specialArray(nums))