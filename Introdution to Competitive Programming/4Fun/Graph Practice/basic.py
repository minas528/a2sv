graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()
count = 0
from collections import deque

stack = deque()


def dfs(graph_input, stack, visited_set, node, to_find, depth):
    visited_set.add(node)
    stack.append(node)
    # print(node, to_find)
    while stack:

        curr = stack.popleft()
        print(curr, to_find)
        if curr == to_find:
            return True, depth
        for nbr in graph_input[curr]:
            if nbr not in visited:
                stack.append(nbr)

    return False, -1


if __name__ == '__main__':
    # a = []
    # for j in range(2000):
    #     a.append(2000)
    # print(a)
    import heapq
    l = [4,2,6,2,7,4,7]
    heapq.heappush(l,10)
    heapq.heapify(l)
    print(heapq.heapreplace(l,3))
    print(l)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        sum = []
        self.helper(root, sum)
        return sum[0]

    def helper(self, root, sum):
        if not root:
            return [0, 0]
        left = self.helper(root.left, sum)
        right = self.helper(root.right, sum)
        curr_sum = abs(left[0] - left[1]) + abs(right[0] - right[1])
        sum[0] += curr_sum
        left[0] = left[0] + right[0] + 1
        left[1] = left[1] + right[1] + root.val
        return left
