from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if(len(height)<=1):
            return -1
        l,r=0,len(height)-1
        v=0
        while(l<r):
            v_new=(r-l)*min(height[l],height[r])
            v=max(v,v_new)
            # 消除短板效应，哪个板子短移动哪个指针
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return v

if __name__ == '__main__':
    h=[1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(h))