# Last updated: 6/7/2025, 11:33:32 PM
class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(1, num+1):
            digits = [int(d) for d in str(i)]

            if sum(digits) % 2 == 0:
                count += 1
        
        return count
            