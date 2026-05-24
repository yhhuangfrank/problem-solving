class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        for i in range(n):
            self.parents[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.parents[n]
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 >= r2:
            self.parents[p2] = p1
            self.rank[p1] += r2
        else:
            self.parents[p1] = p2
            self.rank[p2] += r1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        mst = []
        minHeap = []

        for n1, n2, weight in edges:
            heapq.heappush(minHeap, (weight, n1, n2))
        
        while minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
            if not uf.union(n1, n2):
                continue
            mst.append(w)

        return sum(mst) if len(mst) == n - 1 else -1

