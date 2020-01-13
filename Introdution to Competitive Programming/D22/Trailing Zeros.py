class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n>=5:
            zeros = zeros + n//5
            n = n//5
        return zeros
 
if __name__ == "__main__":
	sol = Solution()
	so.trailingZeros(10)
