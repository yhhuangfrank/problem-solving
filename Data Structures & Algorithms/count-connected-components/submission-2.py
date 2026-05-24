class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        count = 0

        def dfs(cur, prev):
            if cur in visit:
                return False
            visit.add(cur)
            for neigh in adj[cur]:
                if neigh == prev:
                    continue
                dfs(neigh, cur)
            return True
        
        for i in range(n):
            if dfs(i, -1):
                count += 1
        return count