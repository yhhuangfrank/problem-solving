class UnionFind:
    def __init__(self, numNodes):
        self.parent = {}
        self.rank = {}
        for i in range(numNodes):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n1):
        p = self.parent[n1]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:
            return False
        
        uf = UnionFind(n)
        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return False
        return True

