class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using sum
        lst = [n for n in range(len(nums) + 1)]
        return sum(lst) - sum(nums)