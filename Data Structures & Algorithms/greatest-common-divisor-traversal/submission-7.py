class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        num_set = set(nums)
        n = len(num_set)
        if 1 in num_set:
            return len(nums) == 1
        uf = UnionFind()

        prime_factors = set()
        for num in num_set:
            uf.add(num)
            cur = num
            i = 2
            while i * i <= cur:
                if cur % i == 0:
                    if i not in prime_factors:
                        prime_factors.add(i)
                        uf.add(i)
                    while cur % i == 0:
                        cur //= i
                    uf.union(num, i)
                i += 1
            if cur > 1:
                # cur is the last prime factor
                if cur not in prime_factors:
                    prime_factors.add(cur)
                    uf.add(cur)
                uf.union(num, cur)
        # print(prime_factors)
        # print(uf.parent)
        # print(uf.num_of_group)
        return uf.num_of_group == 1

class UnionFind:
    
    def __init__(self):
        self.num_of_group = 0
        self.parent = {}
        self.rank = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            self.num_of_group += 1

    def find(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, a, b):
        p1, p2 = self.find(a), self.find(b)
        if p1 == p2:
            return False
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 >= r2:
            self.parent[p2] = p1
            self.rank[p1] = r1 + r2
        elif r2 > r1:
            self.parent[p1] = p2
            self.rank[p2] = r1 + r2
        self.num_of_group -= 1
        return True
