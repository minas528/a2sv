class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0 :return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2 :
            if max(nums) < (nums[0]+nums[1]):
                return sum(nums)
            return max(nums)
        dp = [None]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]= max(dp[i-1]+nums[i],nums[i])
        print(dp)
        return max(dp)