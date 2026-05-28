class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        lst = []
        orignal_num = x
        x = abs(x)
        while x > 0:
            number = x % 10
            lst.append(number)
            x //= 10
            count += 1
        
        if count > 31:
            return 0
        res = 0
        for n in lst:
            res = res * 10 + n
        
        if not (-1) * 2**31 <= res <= 2**31 - 1:
            return 0
        return res if orignal_num >= 0 else -res
