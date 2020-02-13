# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# import collections
class Solution:
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        ### DFS Implementaion
        # res,stack = [],[(root,0)]
        # while stack:
        #     node,level = stack.pop(0)
        #     if node:
        #         if len(res)== level:
        #             res.append(node.val)
        #         stack.append((node.left,level+1))
        #         stack.append((node.right,level+1))
        # return res 
        
        ##Let's Implement this with BFS
        
        res, que = [], [(root, 0)]
        while que:
            node, level = que.pop(0)
            if node:
                if len(res) == level:
                    res.append(node.val)
                que.append((node.right, level+1))
                que.append((node.left, level+1))
        return res
        
    
    