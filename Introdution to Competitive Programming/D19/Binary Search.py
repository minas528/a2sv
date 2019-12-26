class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums :
            return -1
        def recSearch(nums,target,left,right):
            if left>right :
                return -1
            mid = (left+right)//2
            if target == nums[mid] :
                return mid
            elif target<nums[mid]:
                return recSearch(nums,target,left,mid-1)
            else:
                return recSearch(nums,target,mid+1,right)
        return recSearch(nums,target,0,len(nums)-1)
        
