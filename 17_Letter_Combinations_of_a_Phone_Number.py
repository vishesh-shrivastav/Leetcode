class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        
        letter_map = {
            '2' : ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def backtrack(, digits):
            if len(digits) == 0:
                result.append(combination)
            else:
                for letter in letter_map[digits[0]]:
                    backtrack(combination+letter, digits[1:])
        
        if digits:
            backtrack("", digits)
        
        return result
