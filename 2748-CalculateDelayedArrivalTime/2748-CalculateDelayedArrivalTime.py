# Last updated: 6/7/2025, 11:33:21 PM
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        total = arrivalTime + delayedTime

        return total % 24