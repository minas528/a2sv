# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        self.traversePostorder(root,arr)
        return arr
    def traversePostorder(self,root:TreeNode,res:List[int]):
        if root == None:
            return res
        self.traversePostorder(root.left,res)
        self.traversePostorder(root.right,res)
        res.append(root.val)