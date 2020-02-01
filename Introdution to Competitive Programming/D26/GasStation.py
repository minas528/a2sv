class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ind = -1
        sums = 0
        ctr = 1
        tot = sum(gas) - sum(cost)
        if (tot < 0):
            return -1
        for i in range(len(gas)):
            cur = gas[i] - cost[i]
            sums += gas[i] - cost[i]
            # print(ind)
            if (cur >= 0 and ctr):
                ind = i
                ctr = 0
            if (sums >= 0 and ind < 0):
                ind = i
            elif (sums < 0):
                ind = -1
                sums = 0
        return ind

