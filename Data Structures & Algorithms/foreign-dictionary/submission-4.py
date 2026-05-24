class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()

        for l in range(len(words)):
            r = l + 1
            if r < len(words):
                w1, w2 = words[l], words[r]
                minLen = min(len(w1), len(w2))
                if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                    return ""
                for i in range(minLen):
                    c1, c2 = w1[i], w2[i]
                    if c1 != c2:
                        adj[c1].add(c2)
                        break
        
        res = []
        visit = set()
        path = set()
        
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            visit.add(node)
            path.add(node)
            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            path.remove(node)
            res.append(node)
            return True

        for c in adj.keys():
            if not dfs(c):
                return ""

        output = ""
        for c in res[::-1]:
            output += c
        return output
