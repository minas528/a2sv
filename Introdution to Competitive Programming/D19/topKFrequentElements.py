class Solution:
    def topKFrequent(self, nums, k: int):
        dict_ ={}
        for i in range(len(nums)):
            if nums[i] in dict_:
                dict_[nums[i]] = dict_[nums[i]]+1
            else: dict_[nums[i]]=1
        sorted_dict = sorted(dict_.items(),key=lambda x:[1])
        print(sorted_dict)
        sorted_dict.reverse()
        res = list()
        for i in range(k):
            res.append(sorted_dict[i][0])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3],1))
