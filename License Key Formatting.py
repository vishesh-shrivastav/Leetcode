# Problem number 482
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.split('-')).upper()
        length = len(S)
        remainder = K if length % K == 0 else length % K 
        current_index = remainder
        result = S[:remainder]
        
        while current_index  < length:
            result += '-' + S[current_index: current_index + K]
            current_index += K
            
        return result
        
