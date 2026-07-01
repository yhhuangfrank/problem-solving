import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)
    res = []
    while max_heap:
        n = -heapq.heappop(max_heap)
        res.append(n)
    return res





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
