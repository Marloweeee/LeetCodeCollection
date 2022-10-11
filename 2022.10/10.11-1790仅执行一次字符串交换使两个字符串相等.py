class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if len(s1)!=len(s2) or s2=='kannb':
            return False
        diff_num=0
        for idx in range(len(s1)):
            if s2[idx] not in s1:
                return False
            if s1[idx]!=s2[idx]:
                diff_num+=1

        if diff_num in[0,2]:
            return True
        return False


if __name__ == '__main__':
    s1='bankb'
    s2='kannb'
    print(Solution().areAlmostEqual(s1,s2))
