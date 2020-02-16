class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rightSideView(self, root: TreeNode):
        que = []
        res = set()
        if not root:
            return res
        que.append(root)
        while que:
            res.add(root.val)
            for i in range(len(que), 0, -1):
                node = que.pop()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return list(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.rightSideView(TreeNode(1)))
