# ,求的是(2的(当前括号的深度-1))的平方的值,
# 如 "(())"当前括号深度为2,所以结果为2**(2-1)=2,
# 而(()(()))的结果为"(()->2**(2-1)+(()))->2**(3-1)=2+4=6

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans,deep=0,0
        for idx,letter in enumerate(s):
            if letter=='(':
                deep+=1
            else:
                deep-=1
            if letter==')' and s[idx-1]=='(':
                if deep!=0:
                    ans+=1<<deep
                else:
                    ans+=1
        return ans

if __name__ == '__main__':
    print(Solution().scoreOfParentheses('(((())))'))

