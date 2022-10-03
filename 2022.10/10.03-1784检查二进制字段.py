class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if '0' not in s:
            return True

        idx=1
        while idx < len(s):
            if s[idx]!='0':
                idx+=1
            else:
                break

        return '1' not in s[idx:]

if __name__ == '__main__':
    s = "110"
    print(Solution().checkOnesSegment(s))

