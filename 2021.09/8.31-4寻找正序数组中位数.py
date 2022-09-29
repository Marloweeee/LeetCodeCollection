from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1=0
        left2=0
        res=[]
        while(left1<len(nums1) and left2<len(nums2)):
            if(nums1[left1]<nums2[left2]):
                res.append(nums1[left1])
                left1+=1
            else:
                res.append(nums2[left2])
                left2+=1
        if(left1==len(nums1)):
            res.extend(nums2[left2:])
        else:
            res.extend(nums1[left1:])
        if(len(res)%2):
            return res[len(res) // 2]
        return (res[len(res)//2]+res[len(res)//2-1])/2

if __name__ == '__main__':
    nums1 = [1, 3,5]
    nums2 = [2,4,6]
    s=Solution()
    print(s.findMedianSortedArrays(nums1,nums2))