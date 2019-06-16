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
