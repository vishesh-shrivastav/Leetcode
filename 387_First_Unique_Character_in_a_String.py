class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        # find the index of character that appears only once
        index = 0
        for k in s:
            if d[k] == 1:
                return index
            else:
                index += 1
        
        return -1
        
