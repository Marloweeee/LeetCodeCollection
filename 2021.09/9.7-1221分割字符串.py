class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        dis=0
        for i in s:
            if i=="R":
                dis+=1
            else:
                dis-=1
            if dis==0:
                ans+=1
        return ans
if __name__ == '__main__':
    s="RLRRLLRLRL"
    print(Solution().balancedStringSplit(s))