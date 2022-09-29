class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)==str(x)[::-1]:
            return True
        return False
if __name__ == '__main__':
    x=-121
    s=Solution()
    print(s.isPalindrome(x))