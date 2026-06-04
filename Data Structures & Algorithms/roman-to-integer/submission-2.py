class Solution:
    def romanToInt(self, s: str) -> int:
        # largest to smallest: add them up
        # smaller before larger: substract smaller
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
            n1, n2 = roman[s[i]], roman[s[i + 1]] if i + 1 < len(s) else 0
            if n1 < n2:
                res += -n1
            else:
                res += n1
        return res

            