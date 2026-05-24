class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        table = {}
        minHeap = [(0, src)]
        adj = {i: [] for i in range(n)}

        for s, d, w in edges:
            adj[s].append((d, w))
        
        while minHeap:
            path, s = heapq.heappop(minHeap)
            if s in table:
                continue
            table[s] = path
            for d, w in adj[s]:
                heapq.heappush(minHeap, (table[s] + w, d))
        
        for i in range(n):
            if i not in table:
                table[i] = -1
        return table