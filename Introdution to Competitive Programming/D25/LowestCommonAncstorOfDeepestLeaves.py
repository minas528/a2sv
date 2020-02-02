# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def dfs(Node):
            if not Node:
                return Node, 0
            if not Node.left and not Node.right:
                return Node, 0
            if not Node.right:
                left, left_depth = dfs(Node.left)
                return left, left_depth + 1
            if not Node.left:
                right, right_depth = dfs(Node.right)
                return right, right_depth + 1

            right, right_depth = dfs(Node.right)
            left, left_depth = dfs(Node.left)
            print(left_depth, right_depth)

            if left_depth > right_depth:
                return left, left_depth + 1
            elif right_depth > left_depth:
                return right, right_depth + 1
            else:
                return Node, left_depth + 1

        return dfs(root)[0]
        # if root.left