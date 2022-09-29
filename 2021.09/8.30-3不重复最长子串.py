class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        res_str=''
        for index,item in enumerate(s):
            if item not in res_str:
                res_str+=(item)
            else:
                while s[index] in res_str:
                    res_str=res_str[1:]
                res_str+=(item)
            if len(res_str)>max_len:
                max_len=len(res_str)
        return max_len

if __name__ == '__main__':
    s=Solution()
    string='dfdv'
    print(s.lengthOfLongestSubstring(string))