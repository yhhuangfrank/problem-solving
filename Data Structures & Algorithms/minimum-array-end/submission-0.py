class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        i = 0
        step = n - 1
        while x > 0 or step > 0:
            cur_bit = x & 1
            if cur_bit == 0:
                # insert postion
                bit_on_step = step & 1
                ans |= (bit_on_step << i)
                step = step >> 1
            i += 1
            x = x >> 1
        
        return ans
