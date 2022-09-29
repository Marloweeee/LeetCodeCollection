
from typing import List

class Solution:

    def permute(self, nums):

        visit = [True for _ in range(len(nums))]
        tmp = nums[:]
        def dfs(position):
            if position == len(nums):
                res.append(''.join(tmp[:]))
                return
            for index in range(0, len(nums)):
                if visit[index]:
                    tmp[position] = nums[index]
                    visit[index] = False
                    dfs(position + 1)
                    visit[index] = True
        res = []
        dfs(0)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        res=Solution().permute(list(p))
        for idx in range(len(s)-len(p)+1):
            if s[idx:idx+len(p)] in res:
                ans.append(idx)
        return ans


if __name__ == '__main__':
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s,p))