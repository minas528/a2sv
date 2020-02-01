class Solution:
    def BFS(self,root,fcn):
        stack = [root]
        while len(stack)>0:
            if fcn[stack[0]]:
                return True
            else:
                temp = stack.pop(0)
                if temp.getRightBranch():
                    stack.insert(0,temp.getRightBranch())
                if temp.getLeftBranch():
                    stack.insert(0,temp.getLeftBranch())
        return False



if __name__ == '__main__':
    tree = {"S":["A","B"],
            "A":["S"],
            "B":["S","C","D"],
            "C":["B","E","F"],
            "D":["B","G"],
            "E":["C"],
            "F":["C"]
            }
    sol = Solution()
    solution,visitedNodes = sol.BFS(["S"])
    print("Optimal Solution: " ,str(solution))
    print("Visited Nodes : ",str(visitedNodes))