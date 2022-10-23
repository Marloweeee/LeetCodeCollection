class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        cur1,cur2=0,0
        len1,len2=len(word1),len(word2)
        res=''

        while cur1<len1 and cur2<len2:
            res+=word1[cur1]+word2[cur2]
            cur1+=1
            cur2+=1
        res+=word1[cur1:] if cur2>=len2 else word2[cur2:]
        return res

if __name__ == '__main__':
    w1='abcd'
    w2='pq'
    print(Solution().mergeAlternately(w1,w2))

