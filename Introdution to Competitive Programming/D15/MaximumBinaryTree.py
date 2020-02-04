# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return
        mi = nums.index(max(nums))
        ret = TreeNode(nums[mi])
        ret.left = self.constructMaximumBinaryTree(nums[:mi])
        if mi+1 < len(nums):
            ret.right = self.constructMaximumBinaryTree(nums[mi + 1:])
        return ret