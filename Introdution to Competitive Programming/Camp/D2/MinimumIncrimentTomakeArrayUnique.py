class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) < 2: return 0
        n = len(A)
        move = 0
        A.sort()
        for i in range(1, n):
            if A[i] <= A[i - 1]:
                move += (A[i - 1] - A[i] + 1)
                A[i] = A[i - 1] + 1
        return move
