class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "_" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            temp = i
            while s[temp] != "_":
                temp += 1
            length = int(s[i: temp])
            res.append(s[temp + 1: temp + 1 + length])
            i = temp + 1 + length
        return res
