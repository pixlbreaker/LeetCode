# Last updated: 6/7/2025, 11:34:06 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(1, numRows + 1):
            row = []
            if i == 1:
                lst.append([1])
            elif i == 2:
                lst.append([1, 1])
            else:
                prev_list = lst[-1]
                row.append(1)
                for j in range(1, len(prev_list)):
                    curr = prev_list[j]
                    prev = prev_list[j-1]
                    added = curr+prev
                    row.append(added)
                row.append(1)
                lst.append(row)

        return lst