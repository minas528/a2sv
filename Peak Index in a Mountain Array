class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        half = len(A)//2
        if A[half] > A[half-1] and A[half]>A[half+1]:
            return half
        elif A[half]>A[half-1]:
            return half + self.peakIndexInMountainArray(A[half:])
        else:
            return self.peakIndexInMountainArray(A[:half+1])
