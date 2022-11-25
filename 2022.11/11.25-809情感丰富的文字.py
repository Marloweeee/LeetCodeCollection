from  typing import List

class Solution:
    def isExpressiveWord(self,s:str,word:str):
        i,j,s_len,word_len=0,0,len(s),len(word)
        while i<s_len and j<word_len:
            if s[i]!=word[j]:
                return False
            ch=s[i]
            cnti,cntj=0,0
            while i<s_len and s[i]==ch:
                cnti+=1
                i+=1
            while j<word_len and word[j]==ch:
                cntj+=1
                j+=1
            if cntj>cnti:
                return False
            if cnti!=cntj and cnti<3:
                return False
        return i==s_len and j==word_len

    def expressiveWords(self, s: str, words: List[str]) -> int:
        ans=0
        for word in words:
            if self.isExpressiveWord(s,word):
                ans+=1

        return ans

if __name__ == '__main__':
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(Solution().expressiveWords(S,words))

