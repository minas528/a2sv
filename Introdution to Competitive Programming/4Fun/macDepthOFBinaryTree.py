# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# ----------------------------------
    # if(root == NULL)
    #     return 0;
    
    # int res = 0;
    # queue<TreeNode *> q;
    # q.push(root);
    # while(!q.empty())
    # {
    #     ++ res;
    #     for(int i = 0, n = q.size(); i < n; ++ i)
    #     {
    #         TreeNode *p = q.front();
    #         q.pop();
            
    #         if(p -> left != NULL)
    #             q.push(p -> left);
    #         if(p -> right != NULL)
    #             q.push(p -> right);
    #     }
    # }
    
    # return res;
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))