class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return -1
        num = nums[0]
        numOfTheAbovenum = nums[nums[0]]
        while num != numOfTheAbovenum:
            num = nums[num]
            numOfTheAbovenum = nums[nums[numOfTheAbovenum]]
        numOfTheAbovenum = 0
        while numOfTheAbovenum != num:
            num = nums[num]
            numOfTheAbovenum = nums[numOfTheAbovenum]
        return num
        
  #test
  if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([3,1,3,4,2]))
