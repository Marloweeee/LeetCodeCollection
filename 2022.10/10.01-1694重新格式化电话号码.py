class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(' ','').replace('-','')
        ans = ''
        print(number)
        if len(number)<=3:
            return number

        else:
            mod_num=len(number)%3
            sub_len=len(number)//3

            if mod_num==0:
                for i in range(sub_len-1):
                    ans+=number[3*i:3*i+3]+'-'
                ans+=number[-3:]
            elif mod_num==2:
                for i in range(sub_len):
                    ans+=number[3*i:3*i+3]+'-'
                ans+=number[-2:]
            else:
                for i in range(sub_len-1):
                    ans+=number[3*i:3*i+3]+'-'
                ans+=number[-4:-2]+'-'+number[-2:]
        return ans

if __name__ == '__main__':
    number = "1-23-45 67888888"
    print(Solution().reformatNumber(number))

