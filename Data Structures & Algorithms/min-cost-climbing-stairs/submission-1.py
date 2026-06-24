class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            if i in dp:
                return dp[i]
            first = cost[i] + dfs(i + 1)
            second = cost[i] + dfs(i + 2)
            dp[i] = min(first, second)
            return dp[i]
        
        return min(dfs(0), dfs(1))