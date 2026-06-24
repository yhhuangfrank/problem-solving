class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        dp = {}
        def dfs(i, M):
            if i >= n:
                return 0
            k = (i, M)
            if k in dp:
                return dp[k]
            res = 0
            # cannot exceed remaing piles
            for x in range(1, min(n - i, 2 * M) + 1):
                j = i + x
                res = max(
                    res,
                    suffix_sum[i] - dfs(j, max(M, x)) # suffix_sum - another's max
                )
            dp[k] = res
            return res
        
        return dfs(0, 1)