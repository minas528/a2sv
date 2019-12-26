# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        left = []
        right = []
        mid = preorder[0]
        for x in preorder[1:]:
            if x < mid:
                left.append(x)
            else:
                right.append(x)
        node = TreeNode(mid)
        if len(left) > 0:
            node.left = self.bstFromPreorder(left)
        if len(right) > 0:
            node.right = self.bstFromPreorder(right)
        return node
