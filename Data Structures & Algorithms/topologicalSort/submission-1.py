class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)
        
        res = []
        visit = set()
        path = set()

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            visit.add(i)
            path.add(i)
            for neigh in adj[i]:
                if not dfs(neigh):
                    return False
            path.remove(i)
            res.append(i)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []

        return res[::-1]