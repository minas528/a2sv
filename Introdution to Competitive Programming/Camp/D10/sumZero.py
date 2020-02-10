class Solution:
    def sumZero(self, n) :
        arr = []
        num = int((n/2)*(-1))
        while len(arr)<n:
            arr.append(num)
            if num!=0:
                arr.append(-num)
            num+=1
        # if n%2==0:
        #     arr.pop(0)
        return arr

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumZero(100))