class Solution:
    def topKFrequent(self, words, k: int) :
        dict_ = {}
        for word in words:
            if word in dict_:
                dict_[word] = dict_[word]+1
            else:
                dict_[word]=1
        sorted_word = sorted(dict_.items(),key=lambda x:x[1])
        sorted_word.reverse()
        res = list()
        # print(sorted_word)
        for i in range(k):
            res.append(sorted_word[i][0])
        res.sort()
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))