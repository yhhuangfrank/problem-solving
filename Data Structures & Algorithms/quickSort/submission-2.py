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
            if e - s + 1 <= 1:
                return
            pivot = pairs[e].key
            left = s
            for i in range(s, e):
                if pairs[i].key < pivot:
                    tmp = pairs[i]
                    pairs[i] = pairs[left]
                    pairs[left] = tmp
                    left += 1
            # swap left and pivot
            tmp = pairs[left]
            pairs[left] = pairs[e]
            pairs[e] = tmp
            # recursive call
            quickSortHelper(s, left - 1)
            quickSortHelper(left + 1, e)

        quickSortHelper(0, len(pairs) - 1)
        return pairs
