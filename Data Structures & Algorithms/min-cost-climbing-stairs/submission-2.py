class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(
                dp[i + 1] if i + 1 < len(dp) else 0,
                dp[i + 2] if i + 2 < len(dp) else 0
            )
        return min(dp[0], dp[1])
        