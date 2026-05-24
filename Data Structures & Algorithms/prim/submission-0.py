class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for src, dst, weight in edges:
            adj[src].append((weight, dst))
            adj[dst].append((weight, src))

        mst = []
        visited = set()
        minHeap = []
        for w, node in adj[0]:
            heapq.heappush(minHeap, (w, 0, node))
        visited.add(0)
        
        while minHeap:
            w, src, dst = heapq.heappop(minHeap)
            if dst in visited:
                continue
            mst.append(w)
            visited.add(dst)
            for weight, node in adj[dst]:
                if node not in visited:
                    heapq.heappush(minHeap, (weight, dst, node))

        if len(mst) != n - 1:
            return -1
        return sum(mst)