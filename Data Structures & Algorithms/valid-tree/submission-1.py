class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap, visited = {i :[] for i in range(n)}, set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neigh in nodeMap[node]:
                if neigh == prev:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        return dfs(0, -1) and len(visited) == n