class Solution:
    def minSetSize(self, arr) :

        dict_ = {}

        for i in range(len(arr)):
            if arr[i] in dict_:
                dict_[arr[i]] = dict_[arr[i]] + 1
            else:
                dict_[arr[i]] = 1

        val = 0
        # print(dict_)
        sorted_dict = sorted(dict_.items(), key=lambda x: x[1])
        i = 0
        sorted_dict.reverse()

        for key, value in sorted_dict:
            if val < len(arr) // 2:
                i+=1
                val += value
            if val >= len(arr) // 2:
                return i
if __name__ == '__main__':
    sol = Solution()
    print(sol.minSetSize([9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]))