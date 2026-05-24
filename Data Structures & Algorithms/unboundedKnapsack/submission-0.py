class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # brute force
        maxProfit = 0
        
        def dfs(i, curr):
            if i == len(profit):
                return 0
            # skip
            tempProfit = dfs(i + 1, curr)
            # include
            if curr - weight[i] >= 0:
                tempProfit = max(tempProfit, profit[i] + dfs(i, curr - weight[i]))
            return tempProfit
        
        return dfs(0, capacity)
        