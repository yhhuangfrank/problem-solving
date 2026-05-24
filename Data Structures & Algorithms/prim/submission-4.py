class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i: [] for i in range(n)}
        for src, dst, w in edges:
            adj[src].append([dst, w])
            adj[dst].append([src, w])

        minHeap = []
        for node, w in adj[0]:
            heapq.heappush(minHeap, (w, 0, node))
        visit = set()
        visit.add(0)
        mst = []

        while minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            mst.append(w)
            visit.add(n2)
            for neigh, w2 in adj[n2]:
                if neigh not in visit:
                    heapq.heappush(minHeap, (w2, n2, neigh))

        return sum(mst) if len(mst) == n - 1 else -1
