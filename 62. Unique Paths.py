class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 :
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
    

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from scipy.special import comb
        s = m + n - 2
        r = m - 1
        return comb(s, r, exact=True)