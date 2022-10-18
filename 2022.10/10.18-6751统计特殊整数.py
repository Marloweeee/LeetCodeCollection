class Solution:

    def countSpecialNumber(self,n:int)->int:
        # 数位DP（记忆化搜索模板）

        s=str(n)# 将整数n转为字符型

        # @cache
        def f(i:int,mask:int,is_limit:bool,is_number:bool)->int:
            '''
            :param i: 表示从第i位开始填数字
            :param mask: 用二进制数组表示前i-1位的集合，表示能构造出的整数数目
            :param is_limit: 表示前面i-1位是否都填了n对应位上的数字，True则第i位至多填到s[i]，否则填到9
            :param is_number: 表示前面i-1位是否填了数字（是否跳过），True则可从0开始，否则继续跳过或者从1开始
            :return: 所有可能的特殊整数（不包含相同数字）
            左移操作：1<<1=2 2<<1=4 4<<1=8 4<<2=16 i<<d=i*2**d
            右移操作：1>>1=0 2>>1=1 4>>1=2 16>>2=4 mod>>d=mod/2**d
            与运算：A与B值均为1时，A、B与的运算结果才为1，否则为0,例如1&1=1 1&0=0 1&4=0
            或运算：A或B值为1时，A、B或的运算结果才为1，否则为0,例如1|1=1 1|0=1 1|4=5 mask|1<<d=mask+2**d
            '''
            if i==len(s):
                return int(is_number)
            res=0
            if not is_number:# 选择跳过，不填数字
                res=f(i+1,mask,False,False)

            up=int(s[i]) if is_limit else 9
            # 枚举要填的数字，枚举的范围取决于is_limit和is_number
            for d in range(1-int(is_number),up+1):
                if mask>>d&1==0:# 判断mask中是否包含d,不包含d时将d所代表的二进制加入到mask
                    res+=f(i+1,mask|(1<<d),is_limit and d==up,True)
            return res
        return f(0,0,True,False)


if __name__ == '__main__':
    print(Solution().countSpecialNumber(20))


