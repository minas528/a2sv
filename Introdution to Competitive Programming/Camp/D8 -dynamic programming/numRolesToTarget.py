class Solution:
    def __init__(self):
        self.memo = {}
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0 and target == 0:
            return 1
        if d == 0 or target == 0 :
            return 0
        
        cur = (d,target)
        if cur in self.memo:
            return self.memo[cur]
        res = 0
        for i in range(1,f+1):
            if target >= i:
                res += self.numRollsToTarget(d-1,f,target-i)
            else: break
        self.memo[cur] = res
        return res%(1000000000+7)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numRollsToTarget(2,6,7))