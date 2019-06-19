class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """My Solution"""
        hash_map = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]
            
        final_list = []
        
        for k,v in hash_map.items():
            final_list.append(v)
        
        return final_list
