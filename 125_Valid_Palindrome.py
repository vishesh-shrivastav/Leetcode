class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        
        while (r > l):
            if not s[l].isalnum(): #since question states only alphanumeric chars to be considered
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        
        return True
