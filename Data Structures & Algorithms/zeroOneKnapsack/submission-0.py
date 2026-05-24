class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dfs(i, cap):
            if i == len(profit):
                return 0
            # skip
            maxProfit = dfs(i + 1, cap)
            # include
            newCap = cap - weight[i]
            if newCap >= 0:
                maxProfit = max(maxProfit, profit[i] + dfs(i + 1, newCap))
            return maxProfit
        
        return dfs(0, capacity)