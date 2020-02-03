class Solution:
    def isMonotonic(self, A):
        maxx = max(A)
        minn = min(A)
        if maxx == A[len(A)-1] and minn ==A[0]:
            for i in range(1,len(A)):
                if A[i]<A[i-1]:
                    return False
        elif maxx == A[0] and minn==A[len(A)-1]:
            for j in range(1,len(A)):
                if A[i]>A[i-1]:
                    return False
        else:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    sol.isMonotonic()
   
