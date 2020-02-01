class Solution:
    def largestProductwith3Elements(self,arr):
        arr.sort()
        product = 1
        if 0 in arr:
            arr.pop(arr.index(0))
        for i in range(3):
            if abs(arr[0]) >= abs(arr[-1]):
                product*=abs(arr[0])
                arr.pop(0)
            else:
                product*=arr[-1]
                arr.pop(-1)
        return product

if __name__ == '__main__':
    sol = Solution()
    print(sol.largestProductwith3Elements([-4, -4,0,5,1, 2, 8]))



