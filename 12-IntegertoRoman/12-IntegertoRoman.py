class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Roman Dictonary
        roman = ""
        romanInt = {1000:'M', 900:'CM', 500: 'D', 400:'CD', 100: 'C', 90:'XC', 50: 'L', 40:'XL', 10: 'X', 9:'IX', 5: 'V', 4:'IV', 1: 'I'}
        remainder = num

        for key in romanInt:

            # gets the value from the dict
            value = romanInt[key]
            div = remainder // key

            # Adds to the string
            if(div <= 3):
                roman += value * div
            
            elif(div == 5):
                roman += ("V" + value)
            elif(div > 5 and div < 9):
                counted = remainder - 5
                roman += ("V" + (counted * "I"))
            else:
                roman += value
            
            remainder = remainder % key

        return roman
        
