class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = curr_max = curr_min = nums[0]
        
        for x in nums[1:]:
            if x < 0:
                temp = curr_min
                curr_min = curr_max
                curr_max = temp
            
            curr_min = min(x, curr_min * x) # similar to Kadane's
            curr_max = max(x, curr_max * x)
            
            if curr_max > global_max:
                global_max = curr_max
            
        return global_max
