class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1 or num <= 0:
            return False
        i, fout = 2, []
        while i <= math.sqrt(num):
            if num % i == 0:
                fout.append(i)
                fout.append(num/i)
            i += 1
        return num == sum(fout)+1
if __name__ == '__main__':
    sol = Solution()
    sol.checkPerfectNumber(28)
