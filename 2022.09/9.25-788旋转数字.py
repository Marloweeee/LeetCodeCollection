class Solution:
    def rotatedDigits(self, n: int) -> int:


        flag,ans=[0,0,1,-1,-1,1,1,-1,0,1],0

        for num in range(1,1+n):
            num=[int(i) for i in str(num)]
            if_347,if_2569=True,False
            for item in num:
                if flag[item]==1:
                    if_2569=True
                if flag[item]==-1:
                    if_347=False
            if if_347 and if_2569:
                ans+=1
        return ans

if __name__ == '__main__':
    print(Solution().rotatedDigits(13))