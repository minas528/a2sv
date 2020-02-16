class Solution:
    def findCircleNum(self, M) -> int:
        circles = 0
        visited = [False] * len(M)

        for i in range(len(M)):
            if not visited[i]:
                circles += 1
                self.dfs(M, visited, i)

        return circles

    def dfs(self, M, visited, i):
        visited[i] = True
        for k in range(len(M)):
            if not visited[k] and M[i][k] == 1:
                self.dfs(M, visited, k)


if __name__ == '__main__':
    sol = Solution()
    answer = sol.findCircleNum([[1, 1, 0],
                                [1, 1, 0],
                                [0, 0, 1]])
    print(answer)
