class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if(grid==None or grid[0]==None): return 0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if j>0:
                    left = grid[i][j-1]
                else:
                    left = -1
                if i>0:
                    top = grid[i-1][j]
                else:
                    top =-1
                if(left == -1 and top ==-1): continue
                elif left == -1 :
                    grid[i][j] += top
                elif top == -1:
                    grid[i][j]+= left
                else:
                    grid[i][j] += min(left,top)
        return grid[n-1][m-1]


