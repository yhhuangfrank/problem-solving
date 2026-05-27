class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        if k == 1:
            return total
        
        max_num = max(nums)
        # max_num <= answer <= total
        # we can use binary search to find the answer
        
        def split(arr, max_per_group):
            groups = 1
            cur = arr[0]
            for i in range(1, len(arr)):
                n = arr[i]
                if cur + n > max_per_group:
                    groups += 1
                    cur = n
                else:
                    cur += n

            return groups
        
        l = max_num - 1 # min of possible answer - 1
        r = total # max of possible answer
        while l + 1 < r:
            mid = (l + r) // 2
            groups = split(nums, mid)
            if groups > k:
                l = mid
            else:
                r = mid

        return l + 1


        