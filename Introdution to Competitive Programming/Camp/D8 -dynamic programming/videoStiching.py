class Solution:
    def videoStitching(self, clips, T: int) -> int:
        dp = [T+1]*(T+1)
        dp[0] = 0
        for i in range(T+1):
            for c in clips:
                if i>= c[0] and i<= c[1] : dp[i] = min(dp[i],dp[c[0]]+1)
                print(i,c[0] , i, c[1],dp[i],dp[c[0]])
            print(dp)
            if dp[i] == T+1: return -1
        print(dp)
        return dp[T]
if __name__ == "__main__":
    sol = Solution()
    print(sol.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10))
    # print(sol.videoStitching([[0,1],[1,2]],5))
    # print(sol.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))
    # [[0,1],[1,2]]
