class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {"]":"[", "}":"{", ")":"("}
        
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            elif ch in mapping:
                if stack == [] or mapping[ch] != stack.pop():
                    return False
            else:
                return False
        
        return stack == []
