class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[-1] * (capacity + 1) for _ in range(len(profit) + 1)]

        def dfs(i, cap):
            if i == len(profit):
                return 0
            if dp[i][cap] != -1:
                return dp[i][cap]
            # skip
            dp[i][cap] = dfs(i + 1, cap)
            # include
            newCap = cap - weight[i]
            if newCap >= 0:
                dp[i][cap] = max(dp[i][cap], profit[i] + dfs(i + 1, newCap))
            return dp[i][cap]
        
        return dfs(0, capacity)
