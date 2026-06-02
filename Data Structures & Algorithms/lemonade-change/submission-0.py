class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 20 -> 15 -> 10 + 5 or 5 * 3
        # 10 -> 5
        lst = [0] * 3 # count for each bill
        for n in bills:
            if n == 5:
                lst[0] += 1
            elif n == 10:
                lst[1] += 1
                if lst[0] == 0:
                    return False;
                lst[0] -= 1
            else:
                lst[2] += 1
                if lst[1] > 0 and lst[0] > 0:
                    lst[1] -= 1
                    lst[0] -= 1
                elif lst[0] >= 3:
                    lst[0] -= 3
                else:
                    return False
        return True