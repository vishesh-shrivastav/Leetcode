class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        h_m = {}
        
        for ch in S:
            if ch in J:
                if ch not in h_m:
                    h_m[ch] = h_m.get(ch, 0) + 1
                else:
                    h_m[ch] += 1
        
        count = 0
        
        for v in h_m.values():
            count += v
        
        return count
        """
        j_set = set(J)
        x = [c in j_set for c in S] # boolean array
        
        """
        For example input:
        J = "aA"
        S = "aAAbbb"
        x = [True, True, True, False, False, False]
        """
        
        return(sum(x))
