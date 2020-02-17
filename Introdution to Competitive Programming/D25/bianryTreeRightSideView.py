# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def rightSideView(self, root: TreeNode):
        # DFS Implementation
        res, stack = [], [(root, 0)]
        while stack:
            node, level = stack.pop(0)
            if node:
                if len(res) == level:
                    res.append(node.val)
                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))
        return res

        # Let's Implement this with BFS


#         res, que = set(), [(root, 0)]
#         while que:
#             # print("queue", que)
#             node, level = que.pop(0)
#             # print(node)
#             if node:
#                 if len(res) == level:
#                     res.add(node.val)
#                 # print(res,level)

#                 que.append((node.right, level+1))
#                 que.append((node.left, level+1))
#         return list(res)


# class ProductOfNumbers {
#     vector<int> product;
#     int zeropos = 0;
# public:
#     ProductOfNumbers() {
#     }
#
# void add(int num) {
#     int size = product.size();
#     if((size>=1&&product[size-1]==0)||size==0) product.push_back(num);
#     else product.push_back(product[size-1]*num);
#     if(num==0) {
#         for(int i = zeropos;i<=size;i++) {
#             product[i] = 0;
#         }
#         zeropos = size;
#     }
# }
#
# int getProduct(int k) {
#     int size = product.size();
#     if(product[size-k]==0) return 0;
#     if(k==size||product[size-1-k]==0) return product[size-1];
#     return product[size-1]/product[size-1-k];
# }
# };


from bisect import bisect_left


class ProductOfNumbers:

    def __init__(self):
        self.zeros = []
        self.arr = [1]

    def add(self, num: int) -> None:
        if num:  # pre-multiply
            self.arr.append(self.arr[-1] * num)
        else:  # record zeros and append previous value to arr
            self.zeros.append(len(self.arr))
            self.arr.append(self.arr[-1])

    def getProduct(self, k: int) -> int:
        # return 0 if zeros found, otherwise calculate product by dividing two pre-products
        return 0 if bisect_left(self.zeros, len(self.arr) - k) < len(self.zeros) else self.arr[-1] // self.arr[-k - 1]


if __name__ == '__main__':
    sol = Solution()
    sol.rightSideView()
