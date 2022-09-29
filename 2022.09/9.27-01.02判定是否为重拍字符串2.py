class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:

        s1=sorted(s1)
        s2=sorted(s2)

        if s1==s2:
            return True
        return False

if __name__ == '__main__':
    s1='aabbjklkjh'
    s2='jklkjhaalb'
    print(Solution().CheckPermutation(s1,s2))
