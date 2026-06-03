class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == 'I':
                cur = 1
                if i + 1 < len(s):
                    if s[i + 1] == 'V':
                        cur *= 4
                        i += 1
                    elif s[i + 1] == 'X':
                        cur *= 9
                        i += 1
            elif c == 'X':
                cur = 10
                if i + 1 < len(s):
                    if s[i + 1] == 'L':
                        cur *= 4
                        i += 1
                    elif s[i + 1] == 'C':
                        cur *= 9
                        i += 1
            elif c == 'C':
                cur = 100
                if i + 1 < len(s):
                    if s[i + 1] == 'D':
                        cur *= 4
                        i += 1
                    elif s[i + 1] == 'M':
                        cur *= 9
                        i += 1
            elif c == 'V':
                cur = 5
            elif c == 'X':
                cur = 10
            elif c == 'L':
                cur = 50
            elif c == 'D':
                cur = 500
            else:
                cur = 1000
            res += cur
            i += 1
        return res