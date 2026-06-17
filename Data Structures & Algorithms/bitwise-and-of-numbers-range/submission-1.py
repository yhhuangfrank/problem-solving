class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 1010 = 8 + 2
        # ...
        # 1100 = 8 + 4
        
        # 101 = 5
        # 100
        # 011
        # 010
        # 001 = 1
        l, r = left, right
        count = 0
        while l != r:
            l = l >> 1
            r = r >> 1
            count += 1
        return l << count
        