class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] * (N + 1)
        dp[0] = False
        dp[1] = False
        for n in range(2, N + 1):
            for i in range(1, n):
                if n % i == 0:
                    dp[n] = dp[n] or not dp[n - i]
                    print(dp[n], dp[n - i], dp)
        return dp[-1]
    # These Can be implemented with math#

    #return N%2
