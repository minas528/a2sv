class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        # grid = [[-1]*len(grid)]*len(grid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        # obstacleGrid[0][0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if (0 <= i - 1 < len(obstacleGrid) and
                        0 <= j - 1 < len(obstacleGrid[0])):
                    print("here", i, j)
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                elif (0 <= i - 1 < len(obstacleGrid)):
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                elif 0 <= j - 1 < len(obstacleGrid[0]):
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 1

        print(obstacleGrid)
        return obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
