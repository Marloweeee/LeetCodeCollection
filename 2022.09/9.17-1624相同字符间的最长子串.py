class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        max_dis=-1

        dic={}
        for idx in range(len(s)):
            if s[idx] not in dic:
                dic[s[idx]]=idx

        for idx in range(len(s)-1,-1,-1):
            if s[idx] in dic:
                max_dis=max(max_dis,idx-dic[s[idx]]-1)


        return max_dis

if __name__ == '__main__':
    print(Solution().maxLengthBetweenEqualCharacters("abcda"))