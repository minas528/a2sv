class Solution:
    def largestSumOfAverages(self, A, K: int) -> float:
        n = len(A)
        sum =[None]*n
        sum[0] = A[0]
        for i in range(1,n): sum[i] = sum[i-1]+A[i]
        arr =[[0]*n]*(K+1)
        print(sum,arr)
        return self.backTrack(A,n,sum,0,K,arr)
    def backTrack(self,A,n,sum,index,K,dp):
        if K==1 : return (sum[n-1]-sum[index]+A[index])/(n-index)
        if dp[index][K]!=0 :return dp[index][K]
        for i in range(index,n-K+1):
            dp[index][K] = max(dp[index][K],(((sum[i]-sum[index] + A[index]*1.0)/(i-index+1))+ self.backTrack(A,n,sum,i+1,K-1,dp)))
        return int(dp[index][K])

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestSumOfAverages([9,1,2,3,9],3))
