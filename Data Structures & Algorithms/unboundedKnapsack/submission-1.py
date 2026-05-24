class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # brute force
        maxProfit = 0
        cache = {}
        
        def dfs(i, curr):
            if i == len(profit):
                return 0
            if (i, curr) in cache:
                return cache[(i, curr)]
            # skip
            cache[(i, curr)] = dfs(i + 1, curr)
            # include
            newCap = curr - weight[i]
            if newCap >= 0:
                cache[(i, curr)] = max(cache[(i, curr)], profit[i] + dfs(i, newCap))
            return cache[(i, curr)]
        
        return dfs(0, capacity)
