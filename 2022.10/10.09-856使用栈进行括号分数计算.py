class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=[0]

        for letter in s:
            if letter=='(':
                ans.append(0)
            else:
                v=ans.pop()
                ans[-1]+=max(2*v,1)

        return ans[-1]
if __name__ == '__main__':
    print(Solution().scoreOfParentheses('()()'))