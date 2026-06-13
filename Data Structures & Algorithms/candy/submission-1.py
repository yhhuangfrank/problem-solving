class Solution:
    def candy(self, ratings: List[int]) -> int:
        min_heap = [] # (rating, index)
        for i, r in enumerate(ratings):
            heapq.heappush(min_heap, (r, i))
        n = len(ratings)
        candies = [1] * n # at least one for each
        while min_heap:
            r, i = heapq.heappop(min_heap)
            left_r = ratings[i - 1] if i - 1 >= 0 else float('inf')
            right_r = ratings[i + 1] if i + 1 < n else float('inf')
            if ratings[i] > left_r and ratings[i] > right_r:
                left_c = candies[i - 1] if i - 1 >= 0 else 0
                right_c = candies[i + 1] if i + 1 < n else 0
                candies[i] = max(left_c, right_c) + 1
            elif ratings[i] > left_r:
                candies[i] = candies[i - 1] + 1
            elif ratings[i] > right_r:
                candies[i] = candies[i + 1] + 1
        return sum(candies)

