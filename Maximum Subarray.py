# Problem number 53
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's Algorithm
        max_curr = max_global = nums[0]
        
        for x in nums[1:]:
            max_curr = max(x, max_curr + x)
            if max_curr > max_global:
                max_global = max_curr
            
        return max_global
        
