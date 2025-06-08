# Last updated: 6/7/2025, 11:33:26 PM
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.8) + 32.00

        return [kelvin, fahrenheit]