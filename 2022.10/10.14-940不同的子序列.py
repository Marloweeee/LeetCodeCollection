class Solution:
    def distinctSubseqII(self, s: str) -> int:

        mod=10**9+7
        f=[[0]*26 for i in range(len(s)+1)]# 状态数组

        for idx,letter in enumerate(s,1):
            letter_idx=ord(letter)-ord('a')# 得到第i个字母在状态数组f[i]中的索引
            f[idx]=f[idx-1].copy()
            f[idx][letter_idx]=(1+sum(f[idx-1]))%mod

        return sum(f[-1])%mod


if __name__ == '__main__':
    print(Solution().distinctSubseqII('aba'))