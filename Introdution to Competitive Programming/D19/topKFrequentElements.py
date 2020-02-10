# List<Integer>[] bucket = new List[nums.length + 1];
# 	Map<Integer, Integer> frequencyMap = new HashMap<Integer, Integer>();

# 	for (int n : nums) {
# 		frequencyMap.put(n, frequencyMap.getOrDefault(n, 0) + 1);
# 	}

# 	for (int key : frequencyMap.keySet()) {
# 		int frequency = frequencyMap.get(key);
# 		if (bucket[frequency] == null) {
# 			bucket[frequency] = new ArrayList<>();
# 		}
# 		bucket[frequency].add(key);
# 	}

# 	List<Integer> res = new ArrayList<>();

# 	for (int pos = bucket.length - 1; pos >= 0 && res.size() < k; pos--) {
# 		if (bucket[pos] != null) {
# 			res.addAll(bucket[pos]);
# 		}
# 	}
# 	return res;
class Solution:
    def topKFrequent(self, nums, k: int):
        bucket = []
        dict_ = {}
        for num in nums:
            if num in dict_:
                dict_[num = dict_[num]+1
            else: dict_[num]=1
        for keys,values in dict_.items():
            if dict_[keys] = None:
                bucket[ke]


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3],1))
