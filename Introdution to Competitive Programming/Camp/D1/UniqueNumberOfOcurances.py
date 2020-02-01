class Solution:
    def uniqueOccurrences(self, arr) :
        occ = {}
        for i in arr:
            if i in occ:
                occ[i] += 1
            else:
                occ[i] = 1

        for i in occ:
            for j in range(len(occ)):
                if occ[i] == occ[arr[j]] and i != arr[j]:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    sol.uniqueOccurrences([1,2,3,4,5,9])