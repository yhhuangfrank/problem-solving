class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use XOR operator
        result = 0
        for n1 in range(len(nums) + 1):
            result ^= n1
        for n2 in nums:
            result ^= n2
        return result