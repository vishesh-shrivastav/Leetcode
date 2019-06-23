# Method 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      s_sorted = sorted(s)
      t_sorted = sorted(t)
      
      return (s_sorted == t_sorted)

# Method 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        
        for letter in s:
            s_dict[letter] = s_dict.get(letter, 0) + 1
        
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        
        return (s_dict == t_dict)

# Method 3
# CTCI
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_counts = [0] * 26
        
        for ch in s:
            char_counts[ord(ch) - ord('a')] += 1
        for ch in t:
            char_counts[ord(ch) - ord('a')] -= 1
            if char_counts[ord(ch) - ord('a')] < 0:
                return False
        
        return True
