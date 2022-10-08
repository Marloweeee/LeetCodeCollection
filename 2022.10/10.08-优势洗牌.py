from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans=[0 for i in range(len(nums1))]
        idx = sorted(range(len(nums1)),key=lambda i:nums2[i])

        nums1.sort()
        left,right=0,len(nums2)-1

        for i,num in enumerate(nums1):
            # print("第{}次比较过程：".format(i))
            if num>nums2[idx[left]]:
                # print("当前使用nums1中的{}与nums2中索引为{}的{}比较".format(num,idx[left],nums2[idx[left]]))
                ans[idx[left]]=num
                left+=1
            else:
                # print("当前使用nums1中的{}与nums2中索引为{}的{}比较".format(num, idx[right], nums2[idx[right]]))
                ans[idx[right]]=num
                right-=1
        return ans
if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    print(Solution().advantageCount(nums1, nums2))
