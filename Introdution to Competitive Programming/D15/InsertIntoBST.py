# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
if __name__ == '__main__':
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key
    def printPostorder(root):

        if root:
            # First recur on left child
            printPostorder(root.left)

            # the recur on right child
            printPostorder(root.right)

            # now print the data of node
            print(root.val)
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        print(printPostorder(root))