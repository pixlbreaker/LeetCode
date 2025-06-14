# Last updated: 6/14/2025, 2:02:24 PM
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = date.split('-')[0]
        month = date.split('-')[1]
        day = date.split('-')[2]

        year = "{0:b}".format(int(year))
        month = "{0:b}".format(int(month))
        day = "{0:b}".format(int(day))

        return year +"-" + month + "-" + day
