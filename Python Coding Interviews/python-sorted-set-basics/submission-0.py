from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    i, j = 0, 0
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1):
            sorted_set.add(nums1[i])
            i += 1
        if j < len(nums2):
            sorted_set.discard(nums2[j])
            j += 1
    return [sorted_set.pop(0) for n in range(1, 4)]


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
