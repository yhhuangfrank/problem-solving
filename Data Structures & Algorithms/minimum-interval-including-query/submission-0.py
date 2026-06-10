class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            min_val = float('inf')
            for s, e in intervals:
                if s <= q <= e:
                    min_val = min(min_val, e - s + 1)
            if min_val == float('inf'):
                min_val = -1
            res.append(min_val)
        return res