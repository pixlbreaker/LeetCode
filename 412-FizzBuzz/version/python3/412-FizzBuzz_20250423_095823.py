# Last updated: 4/23/2025, 9:58:23 AM
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        lst = []

        for i in range(1, n+1, 1):
            if i % 3 == 0 and i %5 == 0:
                lst.append("FizzBuzz")
            elif i % 3 == 0:
                lst.append("Fizz")
            elif i % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        
        return lst