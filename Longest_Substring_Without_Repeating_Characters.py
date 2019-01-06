# Problem number 3
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        # Use list to track current longest subscript 
        # without repeating characters
        foo = []
        # Variables to track current sliding window
        i = 0
        j = 0
        
        while j < len(s):
            if (s[j] not in foo):
                foo.append(s[j])
                j += 1;
                max_length = max(max_length, j - i)
            else:
                foo.remove(s[i])
                i += 1
                
        return max_length
