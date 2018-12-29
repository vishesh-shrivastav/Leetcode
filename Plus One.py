# Problem number 66
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in range(len(digits)):
            number += digits[i] * pow(10, len(digits) - 1 - i)
        res = number + 1
        res_to_list = [int(i) for i in str(res)]
        return res_to_list
