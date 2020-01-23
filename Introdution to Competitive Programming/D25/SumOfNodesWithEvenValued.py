# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        S = [0]
        def dfs(N):
            if N and not N.val % 2:
                if N.left:
                    if N.left.left:  S[0] += N.left.left.val
                    if N.left.right: S[0] += N.left.right.val
                if N.right:
                    if N.right.left:  S[0] += N.right.left.val
                    if N.right.right: S[0] += N.right.right.val
            if N: dfs(N.left), dfs(N.right)
        dfs(root)
        return S[0]
