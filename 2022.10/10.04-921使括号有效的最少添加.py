class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        left_parenthese,right_parenthese=0,0

        for letter in s:
            if letter=='(':
                left_parenthese+=1
            elif left_parenthese>0:
                left_parenthese-=1
            else:
                right_parenthese+=1
        return left_parenthese+right_parenthese
if __name__ == '__main__':
    s = ")))("
    print(Solution().minAddToMakeValid(s))