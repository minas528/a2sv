class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1 or num <= 0:
            return False
        i, sums = 2, []
        while i <= math.sqrt(num):
            if num % i == 0:
                sums.append(i)
                sums.append(num/i)
            i += 1
        return num == sum(sums)+1
if __name__ == '__main__':
    sol = Solution()
    sol.checkPerfectNumber(28)
