# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        def quickSortHelper(s, e):
            if e <= s:
                return
            pivot = pairs[e]
            left = s
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1
            # swap left and pivot
            pairs[left], pairs[e] = pivot, pairs[left]
            # recursive call
            quickSortHelper(s, left - 1)
            quickSortHelper(left + 1, e)

        quickSortHelper(0, len(pairs) - 1)
        return pairs
