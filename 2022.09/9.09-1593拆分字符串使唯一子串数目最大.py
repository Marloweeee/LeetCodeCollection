class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        res,idx=[''],0
        while idx <len(s):
            if s[idx] not in res:
                res.append(s[idx])
                idx+=1
            else:
                tmp=idx
                while s[tmp:idx] in res and idx<len(s):
                    idx+=1
                if s[tmp:idx] not in res:
                    res.append(s[tmp:idx])
        return len(res)-1
if __name__ == '__main__':
    print(Solution().maxUniqueSplit("aba"))