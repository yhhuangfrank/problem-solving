class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # split into twp groups, each group's weight close to total_weight / 2
        total = sum(stones)
        half = total // 2
        dp = [0] * (half + 1)
        
        for i in range(len(stones) - 1, -1, -1):
            for target in range(half, stones[i] - 1, -1):
                res = dp[target] # skip
                if target - stones[i] >= 0:
                    choose = stones[i] + dp[target - stones[i]]
                    res = max(res, choose)
                dp[target] = res
        
        max_weight = dp[half]
        other = total - max_weight
        return abs(max_weight - other)