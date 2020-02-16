class Solution:
    def loudAndRich(self, richer, quiet):
        res = [-1] * len(quiet)
        dict_ = {}
        for i in range(len(quiet)):
            dict_[i] = []

        for cur in richer:
            dict_[cur[1]].append(cur[0])

        # dfs Implementation
        def dfs(i, quiet):
            if res[i] > 0:
                return res
            res[i] = i
            for j in dict_[i]:
                if quiet[res[i]] > quiet[dfs(j, quiet)]:
                    res[i] = res[j]
            return res[i]

        for k in range(len(quiet)):
            dfs(i, quiet)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 0]))
    # dic_ = {1:[1]}
    # print(dic_)

# graph = collections.defaultdict(list)
#         print(graph)
#         # graph = {[]*len(quiet)}
#         for u, v in richer:
#             graph[v].append(u)
#
#         result = []
#         for i in range(len(quiet)):
#             visited = set()
#             stack = [i]
#             minVal = quiet[i]
#             idx = i
#
#             while stack:
#                 node = stack.pop(0)
#                 qVal = quiet[node]
#                 if qVal < minVal:
#                     minVal = qVal
#                     idx = node
#
#                 for edge in graph[node]:
#                     if edge not in visited:
#                         visited.add(edge)
#                         stack.append(edge)
#             result.append(idx)
#
#         return (result)
