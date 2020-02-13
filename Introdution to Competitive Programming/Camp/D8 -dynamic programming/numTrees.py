class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0],dp[1] = 1,1
        for l in range(2,n+1):
            for r in range(1,l+1):
                dp[l] += dp[l-r]*dp[r-1]
        return dp[n]