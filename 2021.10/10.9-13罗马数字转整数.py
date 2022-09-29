class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        highestLevel = 1
        result = 0
        for ch in s[::-1]:
            level = mapping[ch]
            if level >= highestLevel:
                result += level
                highestLevel = level
            else:
                result -= level
        return result