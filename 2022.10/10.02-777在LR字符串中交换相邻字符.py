class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        if start.replace('X','')!=end.replace('X',''):
            return False
        j=0
        for idx,letter in enumerate(start):
            if letter=="X":
                continue
            while end[j]=='X':
                j+=1
            if idx!=j and (letter=='L') == (idx<j):
                return False
            j+=1
        return True
