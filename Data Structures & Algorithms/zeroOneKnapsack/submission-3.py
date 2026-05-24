class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        ROWS, COLS = len(profit), capacity + 1
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            dp[r][0] = 0
        for c in range(COLS):
            if c >= weight[0]:
                dp[0][c] = profit[0]
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = dp[r - 1][c]
                if c - weight[r] >= 0:
                    include = profit[r] + dp[r - 1][c - weight[r]]
                    dp[r][c] = max(dp[r][c], include)
        return dp[-1][-1]
