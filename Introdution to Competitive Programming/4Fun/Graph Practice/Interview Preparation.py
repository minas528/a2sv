import collections
import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjency_matrix = collections.defaultdict(dict)

        for node1, node_2, c in edges:
            adjency_matrix[node1][node_2] = adjency_matrix[node_2][node1] = c

        def bfs(s, distanceThreshold):
            visited = [False] * n
            dist = [float('inf')] * n
            frontier = [(0, s)]
            visited[s] = True
            dist[s] = 0
            while not all(visited) and frontier:
                d, s = heapq.heappop(frontier)
                if d > distanceThreshold: break
                dist[s] = d
                visited[s] = True
                for t in adjency_matrix[s]:
                    if not visited[t]:
                        heapq.heappush(frontier, (d + adjency_matrix[s][t], t))
            return len([d for d in dist if d <= distanceThreshold])

        res = 0
        count = n
        for i in range(n):
            c = bfs(i, distanceThreshold)
            if c <= count:
                res = max(res, i)
                count = c
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.findTheCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4)
    print(ans)