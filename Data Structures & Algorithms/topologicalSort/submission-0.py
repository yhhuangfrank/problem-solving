class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i :[] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
        
        res = []
        visited = set()
        path = set()
        
        def dfs(v):
            if v in path:
                return False
            if v in visited:
                return True
            visited.add(v)
            path.add(v)

            for neighbor in adj[v]:
                if not dfs(neighbor):
                    return False
            res.append(v)
            path.remove(v)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        res.reverse()
        return res
        