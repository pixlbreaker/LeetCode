class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = '0'
        sum = ""
        if len(a) < len(b):
            i = len(b) - len(a)
            a = ('0' * i) + a
        elif len(b) < len(a):
            i = len(a) - len(b)
            b = ('0' * i) + b
        for i in range(len(a)-1, -1 , -1):
            x, y = a[i], b[i]
            if carry == '0':
                if x == '0' and y =='0':
                    sum =  '0' + sum
                    carry = '0'
                elif (x == '1' and y =='0') or (x == '0' and y =='1'):
                    sum = '1' + sum
                    carry = '0'
                else:
                    sum = '0' + sum
                    carry = '1'
            else:
                if x == '0' and y =='0':
                    sum =  '1' + sum
                    carry = '0'
                elif (x == '1' and y =='0') or (x == '0' and y =='1'):
                    sum = '0' + sum
                    carry = '1'
                else:
                    sum = '1' + sum
                    carry = '1'
        if carry == '1':
            sum = carry + sum
        return sum
        