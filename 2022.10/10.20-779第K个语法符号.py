class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n>4:
            f=[[] for i in range(n+1)]
        else:
            f=[[] for i in range(4)]
            f[0],f[1]=[0],[0,1]
            f[2], f[3]=[0,1,1,0],[0,1,1,0,1,0,0,1]

        for idx in range(4,n+1):
            f[idx]=f[idx-1]+f[idx-1][::-1]

        return (f[n-1][k-1])


if __name__ == '__main__':

    print(Solution().kthGrammar(5,7))