# Problem number 7
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x > 0:
            int_as_str = str(x)
        else:
            int_as_str = str(x)[1:]
        """
        Or use abs(x) for above
        """
        
        rev = 0
        for i in range(len(int_as_str)):
            poww = len(int_as_str) - 1 - i
            rev += int(int_as_str[poww]) * (10 ** poww)
        
        # If x is positive and reversed integer is less than 2**31
        if x > 0 and int(rev) < (2 ** 31):
            return int(rev)
        # If x is negative and reversed integet is greater than -2**31
        elif x < 0  and (int(rev) * -1) > -(2 ** 31):
            return (int(rev) * -1)
        else:
            return 0
        
