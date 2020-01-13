class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums)==threshold:
            return max(nums) 
        low, up = math.ceil(sum(nums)/threshold), math.ceil(sum(nums)/(threshold-len(nums)))
        
        if sum ( (x+low-1)//low for x in nums ) <= threshold:
            return low
        while low+1<up: 
            mid = (low+up) // 2
            if  sum ( (x+mid-1)//mid for x in nums ) > threshold: low = mid
            else: up = mid
        return up
