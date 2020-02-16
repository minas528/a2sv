class Solotion:
    def loudAndRich(self, richer, quiet):
        # answer = [-1]*len(quiet)
        # # create a directed graph
        # first ,second = set(),set()
        # indegree =[0]* len(quiet)
        # for ric ,richer in richer:
        #     first[]
        pre, suc = [set() for _ in range(n)], [set() for _ in range(n)]
        indegree = n * [0]
        for x, y in richer:
            suc[x].add(y)
            pre[y].add(x)
            indegree[y] += 1
        # visit the sources (richest people) first
        curr_level = {x for x in range(n) if indegree[x] == 0}
        for x in curr_level:
            answer[x] = x
        while curr_level:
            next_level = set()
            for x in curr_level:
                for y in suc[x]:
                    indegree[y] -= 1
                    # new level of sources after removing the previous sources
                    if indegree[y] == 0:
                        answer[y] = y
                        for p in pre[y]:
                            if quiet[answer[p]] < quiet[answer[y]]:
                                answer[y] = answer[p]
                        next_level.add(y)
            curr_level = next_level
        return answer


if __name__ == '__main__':
    sol = Solotion()
    print(sol.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]))
# Output: [5,5,2,5,4,5,6,7])
