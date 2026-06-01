class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        n = columnNumber
        q = deque()
        base = 26
        while n > 0:
            print(f'n % base: {n % base}')
            q.appendleft(letters[n % base])
            if n % base == 0:
                break
            n //= 26
            
        return ''.join(list(q))