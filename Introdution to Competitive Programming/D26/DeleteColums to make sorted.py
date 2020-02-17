class Solution:
    def minDeletionSize(self, A) -> int:
        counter = 0
        comparator = A[0]
        index = 0
        while index < len(comparator):
            temp_store = A[0][index]
            for i in range(1, len(A)):
                if temp_store > A[i][index]:
                    counter += 1
                    break
                else:
                    temp_store = A[i][index]

            index += 1

        return counter


if __name__ == '__main__':
    sol = Solution()
    sol.minDeletionSize(["abs"])
