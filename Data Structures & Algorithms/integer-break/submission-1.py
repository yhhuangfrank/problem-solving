class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1
        k = 2
        while k <= n:
            avg = n // k
            if n % k == 0:
                res = max(res, avg**k)
            else:
                remain = n % k
                product = (avg + 1)**(remain) * avg**(k - remain)
                res = max(res, product)
            k += 1
        return res