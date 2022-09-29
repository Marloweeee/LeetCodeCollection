class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        p3 = p5 = p7 = 1

        for i in range(2, k + 1):
            num3, num5, num7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(num3, num5, num7)
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
            if dp[i] == num7:
                p7 += 1

        return dp[k]
