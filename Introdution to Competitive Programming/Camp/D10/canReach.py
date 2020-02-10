class Solution:
    def __init__(self):
        self.res = False
        self.visited = set()

    def canReach(self, arr: list[int], start: int) -> bool:

        def isValid(i, visited):
            if (0 <= i <= len(arr) - 1 and i not in visited):
                return True
            return False

        def dfs(start, visited):

            if (self.res):
                return

            if (arr[start] == 0):
                self.res = True

            visited.add(start)

            for i in [start + arr[start], start - arr[start]]:
                if isValid(i, visited):
                    dfs(i, visited)

                    # visited = set()

        # self.res = False
        dfs(start, self.visited)
        return self.res