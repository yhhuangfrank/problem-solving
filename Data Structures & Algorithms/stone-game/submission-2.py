class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        
        def dfs(i, j):
            if i == j:
                return piles[i]
            k = (i, j)
            if k in dp:
                return dp[k]
            pick_left = piles[i] - dfs(i + 1, j)
            pick_right = piles[j] - dfs(i, j - 1)
            dp[k] = max(pick_left, pick_right)
            return dp[k]
        
        dfs(0, len(piles) - 1)
        return dp[0, len(piles) - 1] > 0

        

