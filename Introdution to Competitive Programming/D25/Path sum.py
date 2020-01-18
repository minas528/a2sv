# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        sumNew = sum - root.val
        
        if root.left == None and root.right == None:
            return sumNew == 0
        else:
            return self.hasPathSum(root.left,sumNew) or self.hasPathSum(root.right,sumNew)
