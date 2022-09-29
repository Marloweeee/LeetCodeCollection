class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        no_space_num=0
        for item in S:
            if item!=' ':
                no_space_num+=1
        s=''
        for letter in S:
            if length>0:
                if letter==' ':
                    length-=1
                    s+="%20"
                else:
                    s+=letter
                    length-=1

        if length>0:
            s+='%20'*(length-len(s))

        return s

if __name__ == '__main__':

    print(Solution().replaceSpaces("               ", 5))