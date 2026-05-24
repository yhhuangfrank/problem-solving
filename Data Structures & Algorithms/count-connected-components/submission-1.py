class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.components = n
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
        elif r2 < r1:
            self.parent[p2] = p1
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        self.components -= 1
        return True
    
    def getComponents(self):
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)
        return uf.getComponents()

        