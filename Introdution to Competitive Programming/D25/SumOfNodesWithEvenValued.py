# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root):
        Sum = [0]
        def dfs(Node):
            if Node is not None and  Node.val % 2 ==0 :
                print(Node.val)
                if Node.left is not None:
                    if Node.left.left is not None:
                        Sum[0] += Node.left.left.val
                    if Node.left.right is not None:
                        Sum[0] += Node.left.right.val
                if Node.right is not None:
                    if Node.right.left is not None:
                        Sum[0] += Node.right.left.val
                    if Node.right.right is not None:
                        Sum[0] += Node.right.right.val
            if Node is not None:
                dfs(Node.left), dfs(Node.right)
        dfs(root)
        return Sum[0]

if __name__ == '__main__':
    sol = Solution()
    sol.sumEvenGrandparent([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])