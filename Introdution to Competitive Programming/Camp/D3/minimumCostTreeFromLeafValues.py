class Solution:
    def mctFromLeafValues(self, arr):
        total = 0
        while len(arr) >= 1:

            min_val = arr.index(min(arr))
            if len(arr) == 2:
                total += arr[0] * arr[1]
                return total
            elif min_val == 0:
                total += arr[min_val] * arr[1]
            elif min_val == len(arr)-1:
                total += arr[min_val] * arr[-2]
            else:
                if (arr[min_val] * arr[min_val- 1] < arr[min_val] * arr[min_val + 1]):
                    total += arr[min_val] * arr[min_val - 1]
                else:
                    total += arr[min_val] * arr[min_val + 1]
            arr.pop(min_val)
        return total

if __name__ == '__main__':
    sol = Solution()
    sol.mctFromLeafValues([9,14,6,4,13,12,1,6])