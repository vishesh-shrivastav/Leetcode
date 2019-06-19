class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0 : 1}
        count = 0
        total = 0
        
        for item in nums:
            total += item
            count += hash_map.get(total - k)
            hash_map[total] = hash_map.get(total, 0) + 1
            
        return count
