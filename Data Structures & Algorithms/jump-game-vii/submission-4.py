class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True
        prefix = [0] * len(s)
        prefix[0] = 1
        
        for i in range(1, len(s)):
            if s[i] == '0' and i - minJump >= 0: # 最小跳躍距離
                l, r = max(i - maxJump, 0), max(i - minJump, 0)
                left = prefix[l - 1] if l - 1 >= 0 else 0
                if prefix[r] - left > 0:
                    dp[i] = True
            prefix[i] = prefix[i - 1] + (1 if dp[i] else 0)
        return dp[len(s) - 1]
