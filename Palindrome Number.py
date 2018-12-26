# Problem number 9
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert to string
        string_x = str(x)
        # Reverse string
        reversed_x = ""
        for i in string_x:
            reversed_x = i + reversed_x
        # Check if palindrom
        if (reversed_x == string_x):
            return True
        else:
            return False
