class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #s = {}
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                #s[n] = 1
                s.add(n)
        return False
