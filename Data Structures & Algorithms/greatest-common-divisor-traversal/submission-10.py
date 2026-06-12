class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        factor_to_index = {}
        uf = UnionFind(len(nums))

        for i, num in enumerate(nums):
            cur = num
            f = 2
            while f * f <= cur:
                if cur % f == 0:
                    if f in factor_to_index:
                        uf.union(i, factor_to_index[f])
                    else:
                        factor_to_index[f] = i
                    while cur % f == 0:
                        cur //= f
                f += 1
            if cur > 1:
                # cur is the last prime factor
                if cur in factor_to_index:
                    uf.union(i, factor_to_index[cur])
                else:
                    factor_to_index[cur] = i
        
        return uf.num_of_group == 1

class UnionFind:
    
    def __init__(self, n):
        self.num_of_group = n
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return self.parent[a]

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 >= r2:
            self.parent[p2] = p1
            self.rank[p1] = r1 + r2
        else:
            self.parent[p1] = p2
            self.rank[p2] = r1 + r2
        self.num_of_group -= 1
