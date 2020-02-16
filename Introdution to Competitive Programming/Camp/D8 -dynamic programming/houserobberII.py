class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) ==1: return nums[0]
        if len(nums) == 2: return nums[0] if nums[0]>= nums[1] else nums[1]
        
        fromFirst = [0]*(len(nums)+1)
        fromSecond = [0]*(len(nums)+1)
        fromFirst[1] = nums[0]
        
        for i in range(2,len(nums)+1):
            fromFirst[i] = max(fromFirst[i-1],fromFirst[i-2] + nums[i-1])
            fromSecond[i] = max(fromSecond[i-1],fromSecond[i-2] + nums[i-1])
            print(fromFirst,fromSecond)
        return max(fromFirst[-2],fromSecond[-1])

    