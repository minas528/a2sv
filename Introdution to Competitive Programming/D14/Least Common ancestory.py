# The basic Tree structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        if root.val < p.val and root.val <q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root

if __name__ == '__main__':
    tree = TreeNode(6)
    tree2 = TreeNode(2)
    tree3 = TreeNode(0)
    tree4 = TreeNode(4)
    tree5 = TreeNode(3)
    tree6 = TreeNode(5)
    tree7 = TreeNode(8)
    tree8 = TreeNode(7)
    tree9 = TreeNode(9)

    tree.left = tree2
    tree.right = tree7
    tree8.left = tree8
    tree8.right = tree9
    tree2.left = tree3
    tree2.right = tree4
    tree4.left = tree5
    tree4.right = tree6


    sol = Solution()
    print(sol.lowestCommonAncestor(tree,tree2,tree7).val)
