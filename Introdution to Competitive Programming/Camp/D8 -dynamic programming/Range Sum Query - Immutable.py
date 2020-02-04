class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        dp = [None]*(j-i+1)
        dp[0]=self.nums[i]
        for k in range(1,j-i+1):
            dp[k] = self.nums[i+k]+dp[k-1]
        return dp[-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)