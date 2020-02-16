class Solution:
    def shiftingLetters(self, S: str, shifts) -> str:
        # print(chr(ord('a')+17))
        lst = []
        shifts.reverse()
        max_sum = 0
        for num in shifts:
            max_sum += num
            lst.append(max_sum)
        lst.reverse()
        res =""
        for i in range(len(S)):
            res += (chr(ord(S[i]) + lst[i] ))
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.shiftingLetters('abc',[3,5,9]))
