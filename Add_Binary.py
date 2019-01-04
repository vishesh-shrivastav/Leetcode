# Problem number 67
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert both strings to integers
        # Add the integers
        # Convert result to binary
        a_int = 0
        b_int = 0
        for i in range(len(a)):
            poww = len(a) - 1 - i
            a_int += int(a[i]) * (2 ** poww)
        for i in range(len(b)):
            poww = len(b) - 1 - i
            b_int += int(b[i]) * (2 ** poww) 
        
        sum_int = a_int + b_int
        
        # Convert to binary string and return
        return ("{0:b}".format(sum_int))
