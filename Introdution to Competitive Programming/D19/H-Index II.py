class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        l,r = 0,N-1
        while (l<=r):
            mid = (l+r)//2
            if citations[mid]<N-mid:
                l=mid+1
            elif mid-1>=0 and citations[mid-1]>=N-mid+1:
                r=mid-1
            else:
                return N-mid
        return 0
