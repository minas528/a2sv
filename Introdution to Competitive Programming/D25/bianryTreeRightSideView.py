# class Solution {
# public:
#     vector<int> rightSideView(TreeNode *root) {
#         queue<TreeNode*>mQ;
#         vector<int> ret;
#         if(!root)return ret;
#         mQ.push(root);
#         while(!mQ.empty()){
#             ret.push_back(mQ.back()->val);
#             for(int i=mQ.size();i>0;i--){
#                 TreeNode *tn=mQ.front();
#                 mQ.pop();
#                 if(tn->left)mQ.push(tn->left);
#                 if(tn->right)mQ.push(tn->right);
#             }
#         }
#         return ret;
#     }
# };
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def rightSideView(self, root: TreeNode) :
        que = []
        # que.
        res = set()
        if not root:
            return res
        que.append(root)
        while que:
            res.add(root.val)
            for i in range(len(que),0,-1):
                node = que.pop()
                if(node.left):
                    que.append(node.left)
                if (node.right):
                    que.append(node.right)
        return res
if __name__=="__main__":
    q = []
    q.append(9)
    q.append(29)
    q.append(59)
    q.append(49)
    q.append(20)
#[6,1,null,null,3,2,5,null,null,4]
    q.pop(0)
    print(q[0])
    print(q )
