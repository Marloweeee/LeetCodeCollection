class Solution:
    def fib(self, n: int) -> int:

        if n<2:
            return n
        res = [0] * (n + 1)
        res[0], res[1] = 0, 1
        mod=1e9+7
        for i in range(2,n+1):
            res[i]=(res[i-1]+res[i-2])%mod
        return int(res[n])
if __name__ == '__main__':
    n=0
    print(Solution().fib(n))