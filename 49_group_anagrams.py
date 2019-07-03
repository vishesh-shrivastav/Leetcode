class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for word in strs:
            foo = [0] * 26
            for ch in word:
                foo[ord(ch) - ord('a')] += 1

            tf = tuple(foo) #tuple can be dictionary key, list cannot

            if tf in d:
                d[tf].append(word)
            else:
                d[tf] = [word]
        
        return list(d.values())
