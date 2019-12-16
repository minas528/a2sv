class Solution:
    def tribonacci(self, n: int) -> int:
        tri = {}
        for i in range(n+1):
            if i == 0:
                tri[i] = 0
            elif i == 1 or i == 2:
                tri[i] = 1
            else:
                tri[i] = tri[i-1] + tri[i-2] + tri[i-3]
        return tri[n]
