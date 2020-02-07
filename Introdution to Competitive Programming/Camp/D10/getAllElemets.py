# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.arr = []

    def traverse(self, root1):
        if root1:
            self.arr.append(root1.val)
            self.traverse(root1.left)
            self.traverse(root1.right)
        # print(self.arr)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if root1:
            self.traverse(root1)
        if root2:
            self.traverse(root2)
        self.arr.sort()
        return self.arr