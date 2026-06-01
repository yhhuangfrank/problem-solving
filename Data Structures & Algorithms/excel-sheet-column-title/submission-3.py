class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = columnNumber
        q = deque()
        base = 26
        while n > 0:
            n -= 1
            q.appendleft(letters[n % base])
            n //= 26

        return ''.join(list(q))