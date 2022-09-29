from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return list({'()'})
        res = set()
        for i in self.generateParenthesis(n - 1):
            for j in range(len(i) + 2):
                res.add(i[0:j] + '()' + i[j:])
        return list(res)
if __name__ == '__main__':
    print(Solution().generateParenthesis(10))
