# -*- coding: utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        :param s:待求字符串
        :return: 最长回文子串

        状态转移方程：p[i,j]=p[i+1,j-1] and s[i]==s[j]
        边界条件：p[i,i]=true  p[i,i+1]=s[i]==s[i+1]
        '''
        res=''
        for i in range(len(s)):
            #奇数情况
                l, r = i - 1, i + 1
                while(l>=0 and r<len(s) and s[l]==s[r]):
                    l-=1
                    r+=1
                if(len(res)<r-l-1):
                    res=s[l+1:r]
                    # print('奇数情况',res)
            # 偶数情况
                l, r = i , i + 1
                while (l >= 0 and r < len(s) and s[l]==s[r]):
                    l -= 1
                    r += 1
                if (len(res) < r - l-1):
                    res = s[l+1:r]
                    # print('偶数情况',res,"l={},r={}".format(l,r))
        return res
if __name__ == '__main__':
    s1='cbbd'
    # print(s1[1:3])
    s=Solution()
    print(s.longestPalindrome(s1))