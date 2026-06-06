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
        projects = sorted(zip(capital, profits))
        max_heap = [] # (profit)
        n = len(profits)
        idx = 0

        while k > 0:
            # print(f'cur min heap: {min_heap}')
            # print(f'cur max heap: {max_heap}')
            # print(f'cur_cap: {cur_cap}')
            while idx < n and cur_cap >= projects[idx][0]:
                profit = projects[idx][1]
                heapq.heappush(max_heap, -profit)
                idx += 1

            if max_heap:
                cur_cap += -heapq.heappop(max_heap)
                k -= 1
            else:
                break
        
        return cur_cap
