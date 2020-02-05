class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        dp = [1]*(n)
        for i in range(m-1):
            ctr = 0
            for j in range(n):
                dp[j]=ctr+dp[j]
                ctr = dp[j]
                # print(ctr)
            # print(dp)
        return dp[-1]