class Solution:
    def kWeakestRows(self, mat, k: int) :
        dict_ = dict()
        for i in range(len(mat)):
            dict_[i]=sum(mat[i])
        # print(dict_)
        sorted_dict = sorted(dict_.items(),key=lambda x:x[1])
        res = list()
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.kWeakestRows([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],3))