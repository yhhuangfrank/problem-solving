class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        new_queries = sorted(queries)
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        i = 0
        cache = {}

        for q in new_queries:
            if q in cache:
                continue
            # print(min_heap)
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i][0], intervals[i][1]
                l = e - s + 1
                heapq.heappush(min_heap, (l, e))
                i += 1
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # print(min_heap)
            # print('-------')
            if not min_heap:
                cache[q] = -1
            else:
                cache[q] = min_heap[0][0]
        
        return [cache[q] for q in queries]
            
