class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True
        
        for i in range(1, len(s)):
            if s[i] != '0':
                continue
            for j in range(i - maxJump, i - minJump + 1):
                if 0 <= j <= len(s) - 1 and dp[j]:
                    dp[i] = True
                    break
        return dp[len(s) - 1]
