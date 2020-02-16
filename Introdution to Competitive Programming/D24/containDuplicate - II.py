class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        import collections
        difference_storage = collections.defaultdict()
        # print(difference_storage)
        list_length = len(nums)
        for i in range(list_length):
            if nums[i] not in difference_storage:
                difference_storage[nums[i]] = i
            else:
                difference = abs(i - difference_storage[nums[i]])
                print(difference, k)
                if difference <= k:
                    return True
                else:
                    difference_storage[nums[i]] = i

        return False
