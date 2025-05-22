# Last updated: 5/22/2025, 1:00:10 PM
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        #print(prime)
        return prime[2:n].count(True)
