class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            first = stoneValue[i]
            second = stoneValue[i + 1] if i + 1 < n else 0
            third = stoneValue[i + 2] if i + 2 < n else 0
            pick_one = first - dp[0]
            pick_two = first + second - dp[1]
            pick_three = first + second + third - dp[2]
            res = max(pick_one, pick_two, pick_three)
            dp[2] = dp[1]
            dp[1] = dp[0]
            dp[0] = res

        res = dp[0]
        if res == 0:
            return 'Tie'
        elif res > 0:
            return 'Alice'
        return 'Bob'