class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # split into twp groups, each group's weight close to total_weight / 2
        total = sum(stones)
        target = total // 2
        # print(f'total: {total}')
        dp = [[0] * (target + 1) for _ in range(len(stones) + 1)]
        for i in range(len(stones) - 1, -1, -1):
            for j in range(target, -1, -1):
                skip = dp[i + 1][j]
                res = skip
                if j - stones[i] >= 0:
                    choose = stones[i] + dp[i + 1][j - stones[i]]
                    res = max(skip, choose)
                dp[i][j] = res
        # print(dp)
        max_weight = dp[0][target]
        # print(max_weight)
        others = total - max_weight
        # print(f'others: {others}')
        return abs(max_weight - others)