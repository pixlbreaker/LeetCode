# Last updated: 6/17/2025, 8:05:53 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0

        for i in operations:
            if "+" in i:
                num += 1
            else:
                num -= 1

        return num