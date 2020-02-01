class Solution:
    def maxAbsValExpr(self, arr1, arr2):
        tempMax = [arr1[0] + arr2[0],
                   arr1[0] - arr2[0],
                   -arr1[0] + arr2[0],
                   -arr1[0] - arr2[0]]
        result = 0
        # print("tempmax = ",tempMax)
        for i in range(len(arr1)):
            print("tempmax = ", tempMax)
            curr = [-arr1[i] - arr2[i] + i,
                    -arr1[i] + arr2[i] + i,
                    arr1[i] - arr2[i] + i,
                    arr1[i] + arr2[i] + i]
            print("curr",curr)
            for j in range(4):
                result = max(curr[j] + tempMax[j], result)
            tempMax = [max(tempMax[0], arr1[i] + arr2[i] - i),
                       max(tempMax[1], arr1[i] - arr2[i] - i),
                       max(tempMax[2], -arr1[i] + arr2[i] - i),
                       max(tempMax[3], -arr1[i] - arr2[i] - i)]
        return result

if __name__ == '__main__':
    # sol = Solution()
    # print(sol.maxAbsValExpr([1,2,3,4],[-1,4,5,6]))
    list = []
    list.append(9)
    list.index(0)
    print(list)