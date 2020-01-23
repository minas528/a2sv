class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0] - x[1]), reverse = True)
        ret = 0
        A_left = len(costs) // 2
        B_left = A_left
        costs_len = len(costs)
        
        
        for a in range(costs_len):
            if (costs[a][0] > costs[a][1]):
                if (B_left):
                    ret += costs[a][1]
                    B_left -= 1
                else:
                    ret += costs[a][0]
                    A_left -= 1   
            else:
                if (A_left):
                    ret += costs[a][0]
                    A_left -= 1    
                else:
                    ret += costs[a][1]
                    B_left -= 1
                    
        return ret
