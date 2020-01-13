class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        numOfPrimes = 0
        isPrime = [False, False] + [True] * (n - 2)
        for p in range(2, n):
            if not isPrime[p]:
                continue
            numOfPrimes += 1
            for i in range(p * 2, n, p):
                isPrime[i] = False

        return numOfPrimes
if __name__=='__main__':
    sol = Solution()
    sol.countPrimes(10)
