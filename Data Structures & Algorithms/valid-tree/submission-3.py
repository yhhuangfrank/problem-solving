class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        def dfs(cur, prev):
            if cur in visit:
                return False
            visit.add(cur)
            for node in adj[cur]:
                if node == prev:
                    continue
                if not dfs(node, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
