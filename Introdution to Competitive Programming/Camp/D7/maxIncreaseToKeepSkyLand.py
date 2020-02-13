class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top = []
        side = []
        
        for i in range(len(grid)):
            side.append(max(grid[i]))
        for j in range(len(grid[0])):
            max_ = grid[0][j]
            for k in range(len(grid)):
                # print(grid[k][j])
                if grid[k][j]>=max_:
                    max_= grid[k][j]
            top.append(max_)
        dif = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                dif+=(min(top[a],side[b]) - grid[b][a])
        
        # print(top,side)

        return dif
