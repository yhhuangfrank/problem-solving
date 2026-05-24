class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeMap = {i :[] for i in range(n)}
        visited = set()
        count = 0

        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for neighbor in nodeMap[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, node)
        
        for n1, n2 in edges:
            nodeMap[n1].append(n2)
            nodeMap[n2].append(n1)
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count