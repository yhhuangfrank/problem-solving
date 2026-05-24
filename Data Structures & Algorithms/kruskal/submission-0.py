class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 < r2:
            self.parent[p1] = p2
        elif r1 > r2:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        mst = []
        minHeap = []
        unionFind = UnionFind(n)
        for n1, n2, w in edges:
            heapq.heappush(minHeap, (w, n1, n2))
        
        while len(mst) < n - 1 and minHeap:
            w, n1, n2 = heapq.heappop(minHeap)
            if not unionFind.union(n1, n2):
                continue
            mst.append(w)
        
        return sum(mst) if len(mst) == n - 1 else -1

