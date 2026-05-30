class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        
        def dfs(i, j, isAlice):
            if i == j:
                return (0, 0)
            k = (i, j, isAlice)
            if k in dp:
                return dp[k]
            curA, curB = 0, 0
            if isAlice:
                a1 = dfs(i + 1, j, False)[0]
                a2 = dfs(i, j - 1, False)[0]
                curA += max(piles[i] + a1, piles[j] + a2)
            else:
                b1 = dfs(i + 1, j, True)[1]
                b2 = dfs(i, j - 1, True)[1]
                curB += max(piles[i] + b1, piles[j] + b2)
            dp[k] = (curA, curB)
            return (curA, curB)
        
        a, b = dfs(0, len(piles) - 1, True)
        return a > b

        

