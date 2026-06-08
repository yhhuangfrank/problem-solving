class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # split into twp groups, each group's weight close to total_weight / 2
        total = sum(stones)
        # print(f'total: {total}')
        dp = {}
        def dfs(i, target):
            if i >= len(stones):
                return 0
            if (i, target) in dp:
                return dp[(i, target)]
            skip = dfs(i + 1, target)
            res = skip
            if target - stones[i] >= 0:
                choose = stones[i] + dfs(i + 1, target - stones[i])
                res = max(skip, choose)
            dp[(i, target)] = res
            return res
        
        max_weight = dfs(0, total // 2)
        # print(max_weight)
        others = total - max_weight
        # print(f'others: {others}')
        return abs(max_weight - others)