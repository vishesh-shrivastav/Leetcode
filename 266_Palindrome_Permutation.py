# CTCI 1.4
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = {}
        
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        
        count = 0
        
        for v in counts.values():
            if v%2 == 1: #check if value is odd
                count += 1
            if count > 1:
                return False
        
        return True
        
