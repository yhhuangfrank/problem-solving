class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        q = deque()
        base = 26
        while n > 0:
            n -= 1
            offset = n % base
            q.appendleft(chr(ord('A') + offset))
            n //= 26

        return ''.join(list(q))