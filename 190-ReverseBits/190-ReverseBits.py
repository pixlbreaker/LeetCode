# Last updated: 4/2/2025, 4:56:06 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0

        for _ in range(32):
            bit = n & 1            # Extract the least significant bit
            result = (result << 1) | bit # Append the bit to the result
            n >>= 1                # Right-shift n to process the next bit
        return result