class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        num_set = set(nums)
        num_set_list = list(num_set)
        n = len(num_set_list)
        if 1 in num_set:
            return len(nums) == 1
        uf = UnionFind(num_set_list)
        num_of_group = n

        def is_gcd_greater_than_1(a: int, b: int) -> bool:
            low, high = min(a, b), max(a, b)
            if low == 1 or high == 1:
                return False
            if high % low == 0:
                return True
            divisors = []
            for i in range(2, int(math.sqrt(low) + 1)):
                if low % i == 0:
                    divisors.append(i)
                    divisors.append(low // i)
            for d in divisors:
                if high % d == 0:
                    return True
            return False

        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = num_set_list[i], num_set_list[j]
                if is_gcd_greater_than_1(a, b) and uf.union(a, b):
                    num_of_group -= 1

        return num_of_group == 1

class UnionFind:
    
    def __init__(self, nums):
        self.parent = {}
        self.rank = {}
        for i in nums:
            self.parent[i] = i
            self.rank[i] = 1

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
        return True

        
