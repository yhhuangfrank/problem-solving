class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dp
        maxProfit = 0
        ROWS, COLS = len(profit), capacity + 1
        dp = [[0] * COLS for _ in range(ROWS)]

        for c in range(COLS):
            if c >= weight[0]:
                dp[0][c] = profit[0] * (c // weight[0])

        for r in range(1, ROWS):
            for c in range(1, COLS):
                # skip
                dp[r][c] = dp[r - 1][c]
                # include
                newCap = c - weight[r]
                if newCap >= 0:
                    dp[r][c] = max(dp[r][c], profit[r] + dp[r][newCap])
        return dp[-1][-1]
