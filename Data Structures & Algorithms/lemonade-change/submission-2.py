class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 20 -> 15 -> 10 + 5 or 5 * 3
        # 10 -> 5
        five = 0
        ten = 0
        for n in bills:
            if n == 5:
                five += 1
            elif n == 10:
                ten += 1
                if five == 0:
                    return False
                five -= 1
            else:
                if five >= 1 and ten >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True