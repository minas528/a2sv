from typing import List
import collections
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         def bfs(i, j):
#             q = collections.deque([(i, j)])
#             grid[i][j] = 0
#             res = 0
#             while len(q)>0:
#                 for i in range(len(q)):
#                     (x, y) = q.popleft()
#                     res += 1
#                     for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#                         x2, y2 = x+dx, y+dy
#                         if 0<=x2<n and 0<=y2<m and grid[x2][y2]:
#                             grid[x2][y2] = 0
#                             q.append((x2, y2))
#             return res
#
#         area = [bfs(i, j) for i in range(n) for j in range(m) if grid[i][j]]
#         return max(area) if area else 0

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def dfs(ith_index: int, jth_index: int) -> int:
            print(grid[ith_index][jth_index])
            if 0 <= ith_index <= m and 0 <= jth_index < n and grid[ith_index][jth_index]:
                grid[ith_index][jth_index] = 0
                return 1 + dfs(ith_index + 1, jth_index) + \
                       dfs(ith_index - 1, jth_index) + \
                       dfs(ith_index, jth_index + 1) + \
                       dfs(ith_index, jth_index - 1)
            return 0
        # def dfs(i, j):
        #     if 0 <= i < n and 0 <= j < m and grid[i][j]:
        #         # mark as visited
        #         grid[i][j] = 0
        #         return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        #     return 0
        #
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             res = max(res, dfs(i, j))
        # return res
        # n, m = len(grid), len(grid[0])
        #
        # def dfs(i, j):
        #     if 0 <= i < n and 0 <= j < m and grid[i][j]:
        #         # mark as visited
        #         grid[i][j] = 0
        #         return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        #     return 0
        #
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res


if __name__ == '__main__':
    sol = Solution()
    tst_case = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(sol.maxAreaOfIsland(tst_case))
