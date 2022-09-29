class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)[2:]
        bin_list=list(binary)
        res=''
        for i in range(len(bin_list)):
            if bin_list[i]=='0':
                res+='1'
            else:
                res+='0'
        return
if __name__ == '__main__':
    print(Solution().findComplement(5))