class Solution:
    def reverse(self, x: int) -> int:
        lst = []
        orignal_num = x
        x = abs(x)
        while x > 0:
            number = x % 10
            lst.append(number)
            x //= 10
        
        res = 0
        for n in lst:
            res = res * 10 + n
        if orignal_num < 0:
            res = -res
        if not (-1) * 2**31 <= res <= 2**31 - 1:
            return 0
        
        return res
