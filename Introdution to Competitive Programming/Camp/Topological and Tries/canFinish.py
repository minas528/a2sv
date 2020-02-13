class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ref_lst = [0]*numCourses
        for pre in prerequisites:
            ref_lst[pre[0]] += 1
            
        # print(ref_lst)
        que = []
        visited = set()
        for i in range(len(ref_lst)):
            if 0== ref_lst[i]:
                que.append(i)
                visited.add(i)
        res = []
        # print(ref_lst,que,visited)
        while que:
            curr = que.pop(0)
            res.append(curr)
            for pre in prerequisites:
                if pre[1] == curr:
                    ref_lst[pre[0]] -=1
                if (ref_lst[pre[0]] == 0) and  (pre[0] not in visited):
                    que.append(pre[0])
                    visited.add(pre[0])
                print(visited,que,ref_lst)
        if len(res) == numCourses:
            return True
        return False