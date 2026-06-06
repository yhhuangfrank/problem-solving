class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # (capital, profit)
        # (2, 1), (3, 5), (3, 3), (4, 3), (4, 2)
        # w = 2, k = 4, (2, 1) -> w += 1
        # w = 3, k = 3, (3, 5) -> w += 5
        # w = 8, k = 2, (3, 3) or (4, 3) w += 3
        # w = 11, k = 1, (4, 3) or (3, 3) w += 3
        # w = 14, k = 0
        cur_cap = w
        min_heap = [] # (capital, i)
        max_heap = [] # (profit, i)
        n = len(profits)
        for i in range(n):
            heapq.heappush(min_heap, (capital[i], i))

        while k > 0 and (max_heap or min_heap):
            # print(f'cur min heap: {min_heap}')
            # print(f'cur max heap: {max_heap}')
            # print(f'cur_cap: {cur_cap}')

            while min_heap and cur_cap >= min_heap[0][0]:
                c, i = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-profits[i], i))
            if max_heap:
                cur_cap += -heapq.heappop(max_heap)[0]
                k -= 1
            elif cur_cap < min_heap[0][0]:
                break
        
        return cur_cap
