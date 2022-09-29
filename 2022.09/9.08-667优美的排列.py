from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:

        ans=[]
        for num in range(1,n+1):
            if num<k+2:
                if num%2==1:
                    ans.append(int((num+1)//2))
                else:
                    ans.append(int((k+2)-num/2))
            else:
                ans.append(num)

        return ans

if __name__ == '__main__':
    print(Solution().constructArray(50,17))