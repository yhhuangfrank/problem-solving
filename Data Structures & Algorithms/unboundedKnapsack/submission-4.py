class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dp
        maxProfit = 0
        ROWS, COLS = len(profit), capacity + 1
        dp = [0] * COLS

        for r in range(ROWS):
            newDp = [0] * COLS
            for c in range(1, COLS):
                # skip
                newDp[c] = dp[c]
                # include
                newCap = c - weight[r]
                if newCap >= 0:
                    newDp[c] = max(newDp[c], profit[r] + newDp[newCap])
            dp = newDp
        return dp[-1]
