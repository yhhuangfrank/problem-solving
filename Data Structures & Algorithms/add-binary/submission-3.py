class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        res = []

        def cal(total: int):
            res.append(str(total % 2))
            return total // 2

        while i >= 0 and j >= 0:
            n1, n2 = int(a[i]), int(b[j])
            carry = cal(carry + n1 + n2)
            i -= 1
            j -= 1

        while i >= 0:
            carry = cal(carry + int(a[i]))
            i -= 1
        
        while j >= 0:
            carry = cal(carry + int(b[j]))
            j -= 1
        
        if carry:
            res.append('1')
        return ''.join(res[::-1])
        