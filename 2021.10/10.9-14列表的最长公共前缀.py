from typing import List
'''
利用python的max()和min()，
在Python里字符串是可以比较的，
所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_item=min(strs)
        max_item=max(strs)
        for i,word in enumerate(min_item):
            if max_item[i]!=word:
                return max_item[:i]
        return min_item

if __name__ == '__main__':
    strs=["blower","flow","flight"]
    print(Solution().longestCommonPrefix(strs))