from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        res=[""]
        for letter in s:
            if letter.isalpha():
                res=[a+letter.lower() for a in res]+[a+letter.upper() for a in res]
            else:
                res=[a+letter for a in res]
        return res

if __name__ == '__main__':
    print(Solution().letterCasePermutation('3z4'))