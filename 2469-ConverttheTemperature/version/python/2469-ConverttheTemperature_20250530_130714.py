# Last updated: 5/30/2025, 1:07:14 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.8) + 32.00

        return [kelvin, fahrenheit]