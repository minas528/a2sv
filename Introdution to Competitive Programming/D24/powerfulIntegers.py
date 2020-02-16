class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        visited = set()
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            temp = x ** i + y ** j
            if temp <= bound:
                visited.add(temp)
                if x > 1:
                    stack.append((i + 1, j))
                if y > 1:
                    stack.append((i, j + 1))
        return list(visited)


if __name__ == '__main__':
    sol = Solution()
    print(sol.powerfulIntegers(2, 3, 10))
