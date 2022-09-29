class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle=='':
            return -1
        length=len(needle)
        loc=0
        while loc<=len(haystack)-length:
            if haystack[loc:loc+length]==needle:
                return loc
            else:
                loc+=1
        return -1

if __name__ == '__main__':
    print(Solution().strStr('h','h'))