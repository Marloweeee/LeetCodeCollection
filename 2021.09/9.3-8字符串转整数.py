class Solution:
    def myAtoi(self, s: str) -> int:
        if s[0] in [chr(i) for i in range(65,123)] or s=="":
            return 0
        res=""
        index=0
        flag=0
        while(s[index]==" "):
            index+=1
        while(s[index] not in [chr(i) for i in range(65,123)]):
            if s[index]=="+":
                index+=1
                flag+=1
                continue
            if s[index]=="-":
                flag-=1
                index+=1
                continue
            res+=s[index]
            index+=1
            if index==len(s):
                break
        res=int(float(res))*flag
        if res>=2**31-1:
            return 2**31-1
        elif res<=-2**31:
            return -2**31
        return res
if __name__ == '__main__':
    a="-45"
    s=Solution()
    print(s.myAtoi(a))