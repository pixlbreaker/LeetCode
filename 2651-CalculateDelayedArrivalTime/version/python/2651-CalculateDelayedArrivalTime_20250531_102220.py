# Last updated: 5/31/2025, 10:22:20 AM
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        total = arrivalTime + delayedTime

        return total % 24