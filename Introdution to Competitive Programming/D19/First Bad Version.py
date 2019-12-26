class Solution:
    def firstBadVersion(self, n):
        start, end = 0, n-1
        
        while start <= end:
            mid = (start + end)//2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
